# 🎮 Tic Tac Toe (Python)

A console-based Tic Tac Toe game built using Python and Object-Oriented Programming (OOP) principles.
This project demonstrates clean game logic, input validation, and win/draw detection in a structured way.

---

## 📌 Project Overview

This project implements the classic Tic Tac Toe (X vs O) game for two players in the terminal.
The game runs in a turn-based manner, validates user input, and determines the game outcome based on standard Tic Tac Toe rules.

The main goal of this project is to practice:
- Python fundamentals
- Object-oriented design
- Logical problem solving
- Writing clean and readable code

---

## ✨ Features

- Two-player gameplay (Player X vs Player O)
- Input validation
  - Prevents invalid row/column entries
  - Prevents overwriting already filled cells
- Automatic win detection
  - Rows, columns, diagonals, and anti-diagonals
- Draw detection when all cells are filled
- Clean OOP design
  - Game state handled inside a class
  - Game loop handled separately

---

## 🧠 How the Game Works

- The board is a 3×3 grid initialized with empty cells (-)
- Players take turns entering row and column indices (0–2)
- After every move:
  - The board is updated
  - Win conditions are checked
  - A draw is declared if all 9 moves are played without a winner
- The game ends when a player wins or the match results in a draw

---

## 🛠️ Technologies Used

- Python 3
- Core Python concepts:
  - Classes and objects
  - Conditionals and loops
  - Exception handling
  - Lists and indexing

---

## ▶️ How to Run the Project

1. Clone the repository  
   https://github.com/Pavankasala/Tic-Tac-Toe-game

2. Navigate to the project folder  
   cd Tic-Tac-Toe-game

3. Run the game  
   python tictactoe.py

---

## 📚 What I Learned

- Designing a small game using Object-Oriented Programming
- Managing game state cleanly inside a class
- Writing reusable and readable methods
- Handling user input safely
- Implementing real-world game logic step by step

---

## 🚀 Future Improvements

- Add a replay option
- Implement an AI opponent using the Minimax algorithm
- Build a GUI version using Tkinter or Pygame
- Add unit tests for core game logic

---

## 🧑‍💻 Author

Pavan Sai Kasala  
Learning OOP & Problem Solving
