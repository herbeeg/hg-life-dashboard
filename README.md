# Life Tracking Dashboard

All-in-one dashboard for tracking any life events like **goal setting**, **journaling** and **scheduling.**

Written in Python as a desktop app, leveraging the *tkinter* library.

## Requirements

Any Debian-based Linux distribution  
Python 3.8 or greater (uses the newly introduced "walrus operator")   
tkinter: `sudo apt-get install python3-tk`

## Running

Clone the repository into your chosen directory and initialise the virtual environment in the root directory with `python3 -m venv /env`. Activate your newly created environment with `source ./env/bin/activate`.

To run the application, execute the main file with `python3 main_app.py`.

## Goal setting

Allows the user to set up to four goals which can produce a positive result, by means of delayed gratification. 

![Goal Setting preview](/gifs/intro_goals_opt_75.gif)

For example:

- *Goal 1: Purchase Xbox One*
- *Deadline: 01/12/20*
- *Key Result 1: Find a new full-time job*
- *Key Result 2: Move house*
- *Key Result 3: Release Bit Battle alpha v0.1*

### Known limitations

1. **A specific JSON named file is required to load data for the goal setting view.**  
> The user should instead be able to select a local file if they want to load one or allow new data to be created easily.
2. **When data is loaded from file, the columns are compressed towards the centre of the window.**
> From a purely aesthic point of view, it doesn't fill out the window in the same way as it does when new goals are created from scratch. The grid layout should be re-evaluated and changed from fixing the width of each column.
3. **Data is saved every time a goal is edited.**
> Users are forced to constantly update their local JSON data every time a goal is edited via the dialog box. This doesn't allow for any reverting of changes and data can be lost easily. Users should be allowed to save when they choose to, with a custom location.
4. **Data isn't presented cleanly.**
> The data for each goal could be presented much more cleanly. Due to the way that data is retrieved from the dialog, I had to remove any prefacing of strings (e.g. `'Goal 1: ' + goal['name']`) to prevent duplication during editing.

## Journal

Allows the loading, saving and deleting of text files to get thoughts out onto an "electronic" piece of paper.

![Journal preview](/gifs/intro_journal_opt_75.gif)

For example:

*Day 1*

*This is an example journal entry to use during testing.*

*Here's another thing I did that day with special characters!*

### Known limitations

1. **The UI is quite basic.**
> Maybe that's a good thing as it does exactly what it says on the tin. Two additions could be having a separate title element and including a word count in the UI, just to enrich this element of the application.

## Schedule

## X-Effect

## Learnings