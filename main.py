import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic Tac Toe")
        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.buttons = []
        self.create_widgets()

    def create_widgets(self):
        for r in range(3):
            button_row = []
            for c in range(3):
                button = tk.Button(self.master, text="", font=('Arial', 24, 'bold'),
                                   width=5, height=2,
                                   command=lambda row=r, col=c: self.handle_click(row, col))
                button.grid(row=r, column=c, padx=5, pady=5)
                button_row.append(button)
            self.buttons.append(button_row)

        self.reset_button = tk.Button(self.master, text="Reset Game", command=self.reset_game)
        self.reset_button.grid(row=3, columnspan=3, pady=10)

    def handle_click(self, row, col):
        if self.board[row][col] == "" and not self.check_winner():
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)

            if self.check_winner():
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
            elif all(self.board[r][c] != "" for r in range(3) for c in range(3)):
                messagebox.showinfo("Game Over", "It's a tie!")
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        # Check rows
        for r in range(3):
            if self.board[r][0] == self.board[r][1] == self.board[r][2] != "":
                return True
        # Check columns
        for c in range(3):
            if self.board[0][c] == self.board[1][c] == self.board[2][c] != "":
                return True
        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != "":
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != "":
            return True
        return False

    def reset_game(self):
        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        for r in range(3):
            for c in range(3):
                self.buttons[r][c].config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()