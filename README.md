# Scroll and Screenshot Tool
A tool that automates scrolling and capturing screenshots in a loop, ideal for situations where content requires scrolling to be fully viewed and there's no built-in export functionality. 

This tool can be adapted for any application where information retrieval involves scrolling, such as chat logs.

## Disclaimer and Liability Waiver
### Disclaimer
This software is provided "as is" without any warranties or guarantees of any kind. It is intended for lawful, personal use only. The authors of this software are not responsible for any misuse of the tool or any consequences resulting from its use.

### Legal and Ethical Use
By using this software, you agree to comply with all applicable laws and the terms and conditions of any platform you interact with. You are solely responsible for obtaining any necessary permissions before capturing and sharing any content. Unauthorized use of this tool may result in legal action by third parties, including but not limited to privacy violations, intellectual property infringement, or breach of contract.

### Liability
The authors are not liable for any damages or legal repercussions arising from the use or misuse of this software. By downloading, installing, or using the software, you acknowledge that you are responsible for ensuring that your use is compliant with all relevant laws, regulations, and terms of service.

## Usage

For detailed information and additional options, run the command:

```bash
python scroll-screenshotter.py -h
```

## Requirements

* Python 3 (Make sure you have Python 3 installed on your system)
* Install required libraries using pip:

```bash
pip install -r requirements.txt
```

This command will install all the necessary Python libraries (`requirements.txt` is a file that lists the dependencies) needed for the tool to function.

## Using the Tool

Here's an example of how to use the tool:

```bash
python scroll-screenshotter.py -s 20 -o /Users/eloughlin/Desktop -t <my_run_name>
```

This command will:

* Scroll down 20 times (`-s 20`) after each screenshot.
* Save the screenshots to the specified directory (`-o /Users/eloughlin/Desktop`).
* Name each screenshot with a prefix based on the provided title (`-t <my_run_name>`) followed by a sequence number (e.g., "chat_with_evan_01.jpg", "chat_with_evan_02.jpg", etc.).

## Additional Options

The tool offers various options to customize its behavior:

* **Scrolls per Screenshot (`-s`):** (Required) This option specifies the number of scroll downs (or ups) to perform before capturing a screenshot.

* **Output Directory (`-o`):** (Required) This option defines the directory where the captured screenshots will be saved. 

* **Title (`-t`):** (Required) This option allows you to set a prefix for the screenshot filenames. 

* **Image Quality Percent (`-q`):** (Optional, Default: 60) This option controls the image quality of the saved screenshots. A lower percentage creates smaller file sizes but with a corresponding reduction in image quality.

* **Image Size Percent (`-r`):** (Optional, Default: 60) This option allows you to reduce the size of the saved screenshots by a specified percentage. 

* **Scroll Key (`-k`):** (Optional, Default: "down") This option defines the keyboard key used for scrolling. By default, it's set to "down", but you can change it to "up" if your application requires scrolling up (e.g., chat windows). Refer to PyAutoGUI's documentation ([link to PyAutoGUI documentation](https://pyautogui.readthedocs.io/en/latest/keyboard.html)) for a list of supported keyboard keys and more advanced key settings.  For example, you may need to scroll "up", instead of the default of "down". MAKE SURE YOU SET THE RIGHT KEY**

## Demo

![Screenshot Tool Demo](demo.gif)

Youtube Link: https://youtu.be/WOgt3EsVAUU

