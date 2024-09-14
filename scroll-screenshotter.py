import argparse
import json
import os
import time

import pyautogui as gui
import pyscreeze
import skimage
from PIL import Image, ImageGrab

# File to store user's acceptance of the terms
ACCEPTANCE_FILE = "terms_accepted.json"


def liability_waiver():
    waiver_text = """
    === Disclaimer and Liability Waiver ===

    This software is provided "as is" without any warranties or guarantees of any kind. 
    It is intended for lawful, personal use only. The authors of this software are not responsible 
    for any misuse of the tool or any consequences resulting from its use.

    Legal and Ethical Use:
    By using this software, you agree to comply with all applicable laws and the terms and conditions 
    of any platform you interact with. 
    You are solely responsible for obtaining any necessary permissions before capturing and sharing 
    any content. Unauthorized use of this tool may result in legal action by third parties, 
    including but not limited to privacy violations, intellectual property infringement, or breach of contract.

    Liability:
    The authors are not liable for any damages or legal repercussions arising from the use or misuse of this software. 
    By downloading, installing, or using the software, you acknowledge that you are responsible for ensuring 
    that your use is compliant with all relevant laws, regulations, and terms of service.

    Do you accept these terms and conditions? (yes/no):
    """

    # Check if terms have already been accepted
    if os.path.exists(ACCEPTANCE_FILE):
        with open(ACCEPTANCE_FILE, "r") as f:
            data = json.load(f)
            if data.get("accepted"):
                return  # Terms have already been accepted

    # Display waiver text and get user input
    print(waiver_text)
    while True:
        user_input = input().strip().lower()
        if user_input == "yes":
            # Save the acceptance to a local file
            with open(ACCEPTANCE_FILE, "w") as f:
                json.dump({"accepted": True}, f)
            print("Terms accepted. Continuing with the program...")
            break
        elif user_input == "no":
            print("You must accept the terms to use this software. Exiting.")
            exit(1)
        else:
            print("Please answer 'yes' or 'no'.")


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--scrolls-per-screenshot",
        "-s",
        dest="scrolls_per_screenshot",
        type=int,
        required=True,
        help="Number of scrolls between each screenshot",
    )
    parser.add_argument(
        "--output-dir",
        "-o",
        dest="output_dir",
        type=str,
        required=True,
        help="Output directory for screenshots to be saved",
    )
    parser.add_argument(
        "--title",
        "-t",
        dest="title",
        type=str,
        required=True,
        help="Title for screenshots",
    )

    parser.add_argument(
        "--image-quality-percent",
        "-q",
        dest="quality",
        type=int,
        required=False,
        default=60,
        help="Image quality percentage, lower number means smaller images",
    )

    parser.add_argument(
        "--image-size-percent",
        "-r",
        dest="size_reduction",
        type=int,
        required=False,
        default=60,
        help="Save images as this percent size of original screenshot",
    )

    parser.add_argument(
        "--scroll-key",
        "-k",
        dest="scroll_key",
        type=str,
        required=False,
        default="down",
        help='The key that is pressed to cause a single instance of scrolling. (Default = down). Might be "up" depending on your application. Refer to PyAutoGui for other options.',
    )
    return parser.parse_args()


# Ensure user accepts the terms
liability_waiver()

args = parse_args()

count = 0

print("Focus your application on your monitor.")
print("Starting in...")
for i in range(3):
    print(3 - i)
    time.sleep(1)

last_screenshot_path = None

size_pct = args.size_reduction / 100.0

while True:
    screenshot = None
    screenshot = ImageGrab.grab().convert("RGB")
    screenshot = screenshot.resize(
        (int(screenshot.width * size_pct), int(screenshot.height * size_pct))
    )
    screenshot_path = os.path.join(args.output_dir, f"{args.title}_{count:04}.jpeg")

    screenshot.save(screenshot_path, quality=args.quality)
    print(f"Saved screenshot... {screenshot_path}")

    for _ in range(args.scrolls_per_screenshot):
        gui.press(args.scroll_key)
        time.sleep(0.1)

    # Compare current screenshot with last one to see if nothing changed, if so terminate program
    if last_screenshot_path:

        img1 = skimage.io.imread(screenshot_path, as_gray=True)
        img2 = skimage.io.imread(last_screenshot_path, as_gray=True)

        ssim_value = skimage.metrics.structural_similarity(
            img1,
            img2,
            multichannel=True,
            gaussian_weights=True,
            sigma=1.5,
            use_sample_covariance=False,
            data_range=255,
        )

        if ssim_value > 0.99999:
            print(
                f"2 screenshots found are the same. SSIM_Value = {ssim_value} Stopping program."
            )
            break
        else:
            print(f"SSIM Value = {ssim_value}, continuing program...")

    last_screenshot_path = screenshot_path
    count += 1
