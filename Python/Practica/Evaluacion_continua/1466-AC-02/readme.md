# Connect Four (Conecta 4) - Python Terminal Game

## Overview

This project is a terminal-based implementation of the classic **Connect Four** game, where a human player competes against a CPU with variable intelligence.
The game is written in Python, uses object-oriented programming, and features a clean menu-driven interface, multiple CPU difficulty levels, and robust win/draw detection.

---

## Features

- **6x7 Connect Four board** with clear terminal rendering.
- **Menu system** for player name input and difficulty selection.
- **Three CPU difficulty levels:**
  - **Easy:** CPU picks a random valid column.
  - **Normal:** CPU tries to win or block the player.
  - **Hard:** CPU evaluates the best move, blocks all threats, and plays strategically.
- **Win and draw detection** (horizontal, vertical, and diagonal).
- **Object-oriented design** with classes for Board, Player, CPU logic, Menu, and Utilities.
- **Extensible structure** for adding more features or game modes.
- **Terminal UI improvements** for a better user experience.
- **Comprehensive English documentation and docstrings.**

---

## How to Run

1. **Requirements:**
   - Python 3.10+ (no external dependencies).

2. **Start the game:**
   Run the main game file from the project root:
   ```sh
   python game.py
   ```

---

## Game Logic & CPU AI

- **Board Representation:**
  - 6 rows x 7 columns, internally 0-based indices.
  - User input/output uses 1-based column numbers for clarity.

- **Player vs CPU:**
  - Player enters their name and selects CPU difficulty.
  - CPU logic is modular and can be extended.

- **CPU Difficulty Levels:**
  - **Easy:** Random valid move.
  - **Normal:** Attempts to win or block the player in the next move.
  - **Hard:** Evaluates all possible moves, blocks multiple simultaneous threats, and prioritizes winning moves. Uses lookahead and board evaluation for best play.

- **Win/Draw Detection:**
  - Checks for four in a row horizontally, vertically, or diagonally after each move.
  - Detects draw when the board is full.

---

## Project Structure

```
├── board.py              # Board class: manages the game grid and rendering
├── constants.py          # Game constants (symbols, board size, etc.)
├── game.py               # Main entry point: game loop and menu
├── logic.py              # CPU logic and AI for all difficulty levels
├── menu.py               # Menu system and user input handling
├── player.py             # Player class (human and CPU)
├── utils.py              # Utility functions (win/draw detection, input validation)
├── readme.md             # Project documentation (this file)
```

---

## How to Play

1. Run the game as described above.
2. Enter your name when prompted.
3. Select the CPU difficulty (Easy, Normal, Hard).
4. The board will be displayed. Enter the column number (1-7) to drop your piece.
5. The game alternates turns between the player and CPU until someone wins or the board is full.
6. After the game, you can return to the menu or exit.

---

## Educational Value

- Demonstrates object-oriented programming (OOP) in Python.
- Modular codebase for easy extension and learning.
- Well-documented logic and clear separation of concerns.
- Suitable for students learning Python, OOP, and basic AI/game logic.

---

## License

This project is provided for educational purposes.
