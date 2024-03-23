import pyautogui as gui
import time
import argparse
from PIL import Image
from PIL import ImageGrab
import pyscreeze
import os

import skimage

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--scrolls-per-screenshot', '-s', dest="scrolls_per_screenshot", type=int, required=True,
                    help='Time in minutes to move')
    parser.add_argument('--output-dir', '-o', dest="output_dir", type=str, required=True, 
                help='Output directory for screenshots to be saved')
    parser.add_argument('--title', '-t', dest="title", type=str, required=True,
                    help='')

    parser.add_argument('--image-quality-percent', '-q', dest="quality", type=int, required=False, default=60,
                    help='Image quality percentage, lower number means smaller images')

    parser.add_argument('--image-size-percent', '-r', dest="size_reduction", type=int, required=False, default=60,
                    help='Save images as this percent size of original screenshot')
    return parser.parse_args()

args = parse_args()

count = 0

print("Focus Microsoft Teams on your monitor.")
print("Starting in...")
for i in range(3):
    print(3-i)
    time.sleep(1)

last_screenshot_path = None

size_pct = args.size_reduction / 100.0

while(True):
    screenshot = None
    screenshot = ImageGrab.grab().convert("RGB")
    screenshot = screenshot.resize((int(screenshot.width * size_pct), int(screenshot.height * size_pct)))
    screenshot_path = os.path.join(args.output_dir, f"{args.title}_{count:04}.jpeg")

    screenshot.save(screenshot_path, quality=args.quality)
    print(f"Saved screenshot... {screenshot_path}")
        
    for _ in range(args.scrolls_per_screenshot):
        gui.press('up')
        time.sleep(0.1) 

    # Compare current screenshot with last one to see if nothing changed, if so terminate program
    if last_screenshot_path:
        
        img1 = skimage.io.imread(screenshot_path, as_gray=True)
        img2 = skimage.io.imread(last_screenshot_path, as_gray=True)

        ssim_value = skimage.metrics.structural_similarity(img1, img2, multichannel=True, gaussian_weights=True, sigma=1.5, use_sample_covariance=False, data_range=255)

        if ssim_value > 0.99999:
            print(f"2 screenshots found are the same. SSIM_Value = {ssim_value} Stopping program.")
            break
        else: 
            print(f"SSIM Value = {ssim_value}, continuing program...")
    
    last_screenshot_path = screenshot_path
    count += 1
