**Minesweeper GUI Application**

**Introduction:**
The Minesweeper GUI application is a classic implementation of the popular Minesweeper game using the Tkinter library in Python. The game offers players an engaging and challenging experience where they must reveal cells on a grid, trying to avoid hitting hidden mines.

**Features:**

1. **GUI Interface:** The application provides a user-friendly graphical user interface (GUI) built using the Tkinter library. Tkinter allows the creation of interactive windows and widgets.

2. **User Input:** Users are asked to provide input through entry widgets in the GUI. They need to specify the number of rows, columns, and a difficulty level ranging from 0 to 10. The difficulty level determines the probability of mines being placed on the grid.

3. **Game Board Creation:** Once the user provides valid input, the application generates the game grid with the specified dimensions and difficulty level. Mines are placed randomly on the grid, and the numbers indicating the count of adjacent mines are calculated for each cell.

4. **Grid of buttons:** The heart of the game and the part of it I spent the longest on! :D The grid represents the cells of the game, with each button corresponding to a cell. Players can interact with the game board by clicking on the buttons.

5. **Game Logic:** When a player clicks on a button, the application's game logic puts in work. If the clicked cell contains a mine, the game ends, and a message is displayed, informing the player of their encounter with a mine. If the clicked cell is safe, the application reveals either the adjacent mine count or an empty cell, providing players with clues about nearby mines.

6. **Winning:** The ultimate goal is to reveal all non-mine cells without triggering any mines. When players successfully reveal all safe cells, a congratulatory message is displayed, for sweet, sweet victory!

**Note on Implementation:**

This Minesweeper GUI application holds a special significance as it was my first project during my college journey. The project showcases my initial steps into the world of programming and was the first time I played around with a GUI. I had another version of this on Java I did when I was 14, but that was a simple command line based game. :)
