# Life Tracking Dashboard

All-in-one dashboard for tracking any life events like **goal setting**, **journaling** and **scheduling.**

Written in Python as a desktop app, leveraging the *tkinter* library.

Contact: [admin@jonherbst.dev](mailto:admin@jonherbst.dev)

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

Allows the user to set tasks with 1 hour durations for the course of the week, from a given **start** and **end** date for each day.

![Schedule preview](/gifs/intro_schedule_opt_75.gif)

For example:

- *0800: Exercise*
- *0900: Breakfast*
- *1000: Python development*
- *1100: PHP development*

### Known limitations

1. **The schedule will break if the end date is set at a time before the start date.**
> An oversight on my part but the end date values in the dropdown should be altered dynamically based on what the user chooses for the start date. This should provide adequate functionality and not limit the start date flexibility for the user.
2. **Schedule loading and saving are forced onto a specific file in a specific directory.**
> There isn't a lot of flexibility when it comes to dealing with the filesystem. If the specified file doesn't exist, then the user is presented with a generic warning dialog but continues onto the schedule generation phase for the user. From there, it isn't really clear what the user should do next - the presented UI could be a lot clearer or possible scaffold a default empty schedule instead, in this instance.
3. **Each grid element is limited in what the user can input into it.**
> The user can only fit two or three words into each scheduled hour before the grid begins to get distorted. Having a title element with a max character limit and a description either on hover or on click might be better for the user here for more clarity.
4. **Hour representation is not clear enough for users.**
> Hours in both the grid and the dropdown menus are represented by numbers 0-23 for 00:00 to 23:00 hours. These should be converted accordingly to clear any confusion and formatted better with the grid layout.

## X-Effect

Allows the user to cross off specific routine tasks for the day that they want to help form more positive habits from.

Heavily based on the 7-week journey of willpower that Reddit users discuss [here](https://www.reddit.com/r/theXeffect/).

![X-Effect preview](/gifs/intro_xeffect_opt_75.gif)

For example:

- *Section: Programming*
    - *Python*
    - *Game development*
    - *Personal site development*
- *Section: Hobbies*
    - *Warhammer*
    - *Play guitar*
    - *Reading*

### Known limitations

1. **Section title and row text cannot be edited through the UI.**
> Changes to the text can be made by directly editing the local JSON data but this is far from optimal and not obvious to the user. Possibly opening a dialog on click with a simple entry field for text input would suffice here.
2. **New sections and rows cannot be added through the UI.**
> Similar to the previous point, the schedule itself is rather rigid in structure. All of the changes that can be made are by directly editing the local JSON data and the constraints are not obvious to anyone other than the developer themselves. A much more flexible UI is needed here to enrich the limited experience.
3. **When the next month comes, data will not be loaded due to fixed file naming constraints.**
> When the next month turns over, the application will be looking for a file named `ld_MONTH_YEAR.json` and it won't be found unless the user creates a new local file that follows the required naming convention. Instead, the user should be given the option to generate a new grid view that can be changed for the coming month.
4. **Preserving data from previous months is not automated.**
> When a new month comes around, the previous data should be stored and a new JSON file generated with the correct structure for the user to edit upon opening. It could pull all of the titles and sections from the previous month, under the assumption that the user wants to continue tracking the same thing but that's rather restrictive.
5. **Styling the grid can only be done via direct edits through the local JSON data.**
> The example data provided forces a certain colour scheme for each section based on a hex colour code that assumes that the user understands this. A colour picker could be implemented where a button is attached to each section group and updated in the local JSON data accordingly.
6. **Month progress for each hobby/task is not tracked or displayed in the UI.**
> The grid of checkboxes doesn't give a whole lot of feedback to the user about how many times they've completed a task in that month and users like to see statistics. It could also provide a combined percentage or fraction for each section as well, giving more information to the user about what habits they were able to uphold and which ones fell through that month.
7. **Any data loading errors send the user back to the main menu.**
> From a usability point of view, this doesn't give a great deal of information to the user about what's wrong. Is there a problem with the data? Is it a new bug in the application? More information and options need to be provided to resolve any sticking points or "loops" like these. 
8. **Habits/tasks cannot be changed part-way through a single month.**
> I think this makes sense from a data and continuity point of view. It's far easier to track this and causes all sorts of issues if we have to track multiple renamed tasks on a per-row basis.

## Learnings