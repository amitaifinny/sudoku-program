
# Sudoku Game

This project is a console-based Sudoku game developed in Python with the primary learning objective of improving my software design and modular programming skills.

I approached this project using a structured software development process, beginning with a top-down design of the system. Before writing code, I created a structure chart to define the functions and their relationships, a Data Flow Diagram (DFD) to illustrate how information moves through the program, and pseudocode to plan important algorithms.

After completing the design, I used a bottom-up development approach, implementing and testing individual functions before integrating them into a working Sudoku game. I first developed a functional draft that allowed users to load, edit, and save Sudoku boards. I then expanded the program to include input validation, error handling, and enforcement of Sudoku rules.

Throughout development, I focused on writing readable, maintainable code with clear comments, descriptive function names, and well-defined responsibilities for each function.

The completed program allows users to load Sudoku puzzles from JSON files, enter numbers into a 9x9 grid, validate moves against Sudoku rules, and save their progress.

Key concepts practiced: Top-down design, bottom-up implementation, modularization, structure charts, data flow diagrams, pseudocode, file I/O, input validation, testing, and code maintainability.

## Instructions for Build and Use

Steps to build and/or run the software:

1. Install Python 3 on your computer.
2. Download the Python source code and a compatible Sudoku board JSON file.
3. Open the project folder in Visual Studio Code or another Python-compatible development environment.
4. Run the Python file using `python sudoku.py` (replace `sudoku.py` with your actual filename).

Instructions for using the software:

1. When prompted, enter the filename or path of the Sudoku JSON file.
2. The program will load and display the current Sudoku board.
3. Enter a coordinate such as `B2` to select a square. Lowercase (`b2`) and reversed coordinates (`2B`) are also supported.
4. Enter a number between 1 and 9 to fill the selected square.
5. The program checks whether the square is empty and whether the number follows Sudoku rules.
6. If the move is invalid, an error message will appear, and the program will prompt for another coordinate.
7. Enter `Q` to save your progress to the original JSON file and quit the game.

## Development Environment

To recreate the development environment, you need the following software and/or libraries:

* Python 3
* Visual Studio Code
* Python's built-in `json` module
* A Sudoku board stored in JSON format

No external Python packages are required.

## Useful Websites to Learn More

The following websites provide documentation related to this project:

* [Python Official Documentation](https://docs.python.org/3/)
* [Python JSON Documentation](https://docs.python.org/3/library/json.html)
* [Python Built-in Functions](https://docs.python.org/3/library/functions.html)
* [Sudoku Rules](https://en.wikipedia.org/wiki/Sudoku)

## Future Work

The following are potential improvements and features for future development:

* [ ] Add a graphical user interface.
* [ ] Detect when the Sudoku puzzle has been completed.
* [ ] Allow users to undo previous moves.
* [ ] Add a hint system to help players when they get stuck.
* [ ] Improve file handling to support different save files.
* [ ] Add automated unit tests for coordinate parsing and Sudoku validation.
