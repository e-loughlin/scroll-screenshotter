# Scroll and Screenshot Tool

A tool that does this in a loop:
    1) Scrolls up
    2) Takes a screenshot, saves file to directory

Keeps repeating until two screenshots are the same.


For information and additional options, run `python scroll-screenshotter.py -h`

## Requirements

- Python 3

- Source the virtual environment using `source ./env/bin/activate`

- Install requirements with `pip install -r requirements.txt`

## Using

Example: 


`python scroll-screenshotter.py -s 20 -o /Users/eloughlin/Desktop -t <my_run_name>` will screenshot and save to that directory every time it scrolls 20 times.

Each of the screenshots will be named like "chat_with_evan_01.jpg" etc...
