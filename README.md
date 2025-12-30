# Minesweeper (Tkinter)

A classic implementation of the **Minesweeper** game built with **Python** and the **Tkinter** library for the Graphical User Interface (GUI). This project demonstrates object-oriented programming (OOP) principles and algorithmic logic, such as recursive depth-first expansion.

## 🎮 Features
* **Dynamic Board Generation**: Randomized bomb placement using Python's `random` module.
* **Recursive Reveal**: When a cell with zero neighboring bombs is clicked, the game automatically expands and clears the surrounding area using a recursive algorithm.
* **Flagging System**: Users can right-click to place/remove flags on suspected mine locations.
* **Game State Management**: Automatic detection of win and loss conditions with user notifications.

## 🛠️ Tech Stack
* **Language**: Python
* **GUI Framework**: Tkinter

## 🚀 How to Run
1. Ensure you have **Python 3.x** installed.
2. Clone this repository:
   ```bash
   git clone [https://github.com/YOUR_USERNAME/Minesweeper-Python.git](https://github.com/YOUR_USERNAME/Minesweeper-Python.git)
3. Run the application:
   ```bash
   python Minesweeper.py

## 🧠 Technical Highlights
* **Object-Oriented Design:**: Separating logic into `Cell`, `Board`, and `Minesweeper` classes to ensure modularity.
* **Algorithmic Efficiency:**: Implementing a recursive flood-fill-style algorithm to reveal empty neighboring cells efficiently.
