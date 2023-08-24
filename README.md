**Minesweeper GUI Application**

**Introduction:**
The Minesweeper GUI application is a classic implementation of the popular Minesweeper game using the Tkinter library in Python. The game offers players an engaging and challenging experience where they must reveal cells on a grid, trying to avoid hitting hidden mines.

**Features:**

1. **GUI Interface:** The application provides a user-friendly graphical user interface (GUI) built using the Tkinter library, which is one of the standard GUI libraries for Python. Tkinter allows the creation of interactive windows and widgets, making it suitable for building game interfaces.

2. **User Input:** To start the game, users are prompted to provide input through entry widgets in the GUI. They need to specify the number of rows, columns, and a difficulty level ranging from 0 to 10. The difficulty level determines the probability of mines being placed on the grid.

3. **Game Initialization:** Once the user provides valid input, the application generates the game grid with the specified dimensions and difficulty level. Mines are placed randomly on the grid, and the numbers indicating the count of adjacent mines are calculated for each cell.

4. **Button Grid:** The heart of the game's user interface is the button grid. The grid represents the cells of the game, with each button corresponding to a cell. This dynamic layout allows players to interact with the game by clicking on the buttons.

5. **Game Logic:** When a player clicks on a button, the application's game logic is triggered. If the clicked cell contains a mine, the game ends, and a message is displayed, informing the player of their unfortunate encounter with a mine. If the clicked cell is safe, the application reveals either the adjacent mine count or an empty cell, providing players with clues about nearby mines.

6. **Win Condition:** The ultimate goal is to reveal all non-mine cells without triggering any mines. When players successfully reveal all safe cells, a congratulatory message is displayed, signaling their victory.

**Note on Implementation:**

This Minesweeper GUI application holds a special significance as it was my first project during my college journey. The project showcases my initial steps into the world of programming and graphical interfaces. :)

**Acknowledgments:**

I am incredibly grateful to my mother, whose unwavering support and encouragement were pivotal in the development of this program. Her guidance and unwavering belief my abilities provided a constant source of inspiration, motivating me to overcome challenges and persevere. My teacher told me that the grid of buttons cannot be implemented in Python, and it was thanks to her that I finished this project and implemented the grid of buttons! 

**Note**

I wrote this documentation back in early 2022, so don't mind the less "standard" style. Thank you for reading!
