import tkinter as tk
import random
from tkinter import messagebox


class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.is_bomb = False
        self.is_flagged = False
        self.is_revealed = False
        self.neighbor_bombs = 0


class Board:
    def __init__(self, size, bomb_count):
        self.size = size
        self.bomb_count = bomb_count
        self.cells = [[Cell(x, y) for y in range(size)] for x in range(size)]
        self._place_bombs()
        self._calculate_neighbors()

    def _place_bombs(self):
        positions = random.sample([(x, y) for x in range(self.size) for y in range(self.size)], self.bomb_count)
        for x, y in positions:
            self.cells[x][y].is_bomb = True

    def _calculate_neighbors(self):
        for x in range(self.size):
            for y in range(self.size):
                if not self.cells[x][y].is_bomb:
                    count = 0
                    for dx, dy in [(-1, -1),(-1, 0),(-1, 1),(0, -1),(0, 1),(1, -1),(1, 0), (1, 1)]:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < self.size and 0 <= ny < self.size:
                            if self.cells[nx][ny].is_bomb:
                                count += 1
                    self.cells[x][y].neighbor_bombs = count


class Minesweeper:
    def __init__(self, root, size, bomb_count):
        self.root = root
        self.board = Board(size, bomb_count)
        self.buttons = []
        self._create_widgets()

    def _create_widgets(self):
        for x in range(self.board.size):
            row = []
            for y in range(self.board.size):
                btn = tk.Button(self.root, width=2, height=1, bg="light gray",
                                command=lambda x=x, y=y: self._reveal_cell(x, y))
                btn.bind("<Button-3>", lambda e, x=x, y=y: self._toggle_flag(x, y))
                btn.grid(row=x, column=y)
                row.append(btn)
            self.buttons.append(row)

    def _reveal_cell(self, x, y):
        cell = self.board.cells[x][y]
        if cell.is_flagged or cell.is_revealed:
            return
        if cell.is_bomb:
            self.buttons[x][y].config(text='B', bg='red')
            self._game_over(False)
        else:
            self._reveal_recursive(x, y)
            if self._check_win():
                self._game_over(True)

    def _toggle_flag(self, x, y):
        cell = self.board.cells[x][y]
        if cell.is_revealed:
            return
        cell.is_flagged = not cell.is_flagged
        self.buttons[x][y].config(bg="yellow" if cell.is_flagged else "light gray", text='F' if cell.is_flagged else '')

    def _reveal_recursive(self, x, y):
        cell = self.board.cells[x][y]
        if cell.is_revealed or cell.is_bomb:
            return

        cell.is_revealed = True
        self.buttons[x][y].config(bg="white", state=tk.DISABLED,
                                  text=str(cell.neighbor_bombs) if cell.neighbor_bombs > 0 else "")
        if cell.neighbor_bombs == 0:
            for dx, dy in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
                if 0 <= x + dx < self.board.size and 0 <= y + dy < self.board.size:
                    self._reveal_recursive(x + dx, y + dy)

    def _check_win(self):
        for row in self.board.cells:
            for cell in row:
                if not cell.is_bomb and not cell.is_revealed:
                    return False
        return True

    def _game_over(self, won):
        for x in range(self.board.size):
            for y in range(self.board.size):
                cell = self.board.cells[x][y]
                if cell.is_bomb:
                    self.buttons[x][y].config(bg="red", text='B')
        message = "You won!" if won else "You lost!"
        messagebox.showinfo("Game Over", message)
        self.root.quit()


if __name__ == "__main__":
    root = tk.Tk()
    game = Minesweeper(root, size=10, bomb_count=10)
    root.mainloop()
