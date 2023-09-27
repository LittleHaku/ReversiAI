import time
import tkinter as tk
from tkinter import messagebox
from reversi_logic import ReversiGame

# Constants for the colors
BLACK = "#131221"
LAVANDA = "#8b87e0"
WHITE = "#edfff5"


class ReversiGUI:
    """Class to implement the GUI for the Reversi Game"""

    def __init__(self, root):
        self.root = root
        self.root.title("Reversi Game")
        self.game = ReversiGame()
        self.canvas = tk.Canvas(root, width=400, height=400, bg=BLACK)
        self.canvas.pack()
        self.draw_board()
        self.canvas.bind("<Button-1>", self.handle_click)

        self.current_player_label = tk.Label(
            root, text="Current Player: White"
        )

        self.current_player_label.pack()

        self.root.protocol("WM_DELETE_WINDOW", self.confirm_quit)

    def confirm_quit(self):
        """Display a confirmation dialog when leaving the game"""
        user_response = messagebox.askyesno(
            "Quit Confirmation", "Are you sure you want to leave the game?"
        )
        if user_response:
            self.root.quit()

    def draw_board(self):
        for row in range(self.game.board_size):
            for col in range(self.game.board_size):
                x1, y1 = col * 50, row * 50
                x2, y2 = x1 + 50, y1 + 50
                self.canvas.create_rectangle(
                    x1, y1, x2, y2, fill=LAVANDA, outline=WHITE
                )
                if self.game.board[row][col] == "B":
                    self.canvas.create_oval(
                        x1 + 5,
                        y1 + 5,
                        x2 - 5,
                        y2 - 5,
                        fill=BLACK,
                        outline=BLACK,
                    )
                elif self.game.board[row][col] == "W":
                    self.canvas.create_oval(
                        x1 + 5,
                        y1 + 5,
                        x2 - 5,
                        y2 - 5,
                        fill=WHITE,
                        outline=WHITE,
                    )

    def handle_click(self, event):
        col = event.x // 50
        row = event.y // 50
        if (row, col) in self.game.get_valid_moves():
            self.handle_move(col, row)

    def handle_move(self, col, row):
        self.game.make_move(row, col)
        self.move_made()

        if self.game.current_player == "B" and not self.game.is_game_over():
            self.handle_ai_move()

    def handle_ai_move(self):
        print("AI Turn")
        # Force Tkinter to update the screen
        self.root.update_idletasks()
        # time.sleep(0.5)
        self.game.ai_move()
        self.move_made()

    def move_made(self):
        self.draw_board()

        if self.game.current_player == "W":
            self.current_player_label.config(text="Current Player: White")
        elif self.game.current_player == "B":
            self.current_player_label.config(text="Current Player: Black")

        if self.game.is_game_over():
            self.handle_game_over()

    def handle_game_over(self):
        winner = self.game.get_winner()
        if winner == "Tie":
            result = "It's a tie!"
        else:
            result = winner + " wins!"
        self.current_player_label.config(text=result)
        self.canvas.unbind("<Button-1>")
