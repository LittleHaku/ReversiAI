"""""
Reversi Implementation using Tkinter for GUI
    Authors: Iván del Horno Sotillo
"""

import tkinter as tk
from tkinter import messagebox

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

        if self.game.current_player == "W":
            self.current_player_label = tk.Label(
                root, text="Current Player: White"
            )
        elif self.game.current_player == "B":
            self.current_player_label = tk.Label(
                root, text="Current Player: Black"
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
            self.game.make_move(row, col)
            self.draw_board()
            if self.game.current_player == "W":
                self.current_player_label.config(text="Current Player: White")
            elif self.game.current_player == "B":
                self.current_player_label.config(text="Current Player: Black")

            if self.game.is_game_over():
                winner = self.game.get_winner()
                if winner == "Tie":
                    result = "It's a tie!"
                else:
                    result = winner + " wins!"
                self.current_player_label.config(text=result)
                self.canvas.unbind("<Button-1>")  # Disable further clicks


class ReversiGame:
    """Reversi Game Class"""

    def __init__(self):
        """Constructor, initializes the game with a board of 8x8 and the
        initial pieces in the center, also sets the current player to white"""
        self.board_size = 8
        self.board = [
            [" " for _ in range(self.board_size)]
            for _ in range(self.board_size)
        ]
        # Initial pieces
        self.board[3][3] = "W"
        self.board[3][4] = "B"
        self.board[4][3] = "B"
        self.board[4][4] = "W"
        self.current_player = "W"

    def is_valid_move(self, row, col):
        """Checks if the move to a certain cell is valid or not, it will check
        if its between the boundaries of the board and if the cell is empty
        and also if it will flip any pieces"""
        if (
            # Check if the cell is beyond the board or not empty
            not (0 <= row < self.board_size)
            or not (0 <= col < self.board_size)
            or self.board[row][col] != " "
        ):
            return False
        return self.is_flippable(row, col)

    def is_flippable(self, row, col):
        """Check if the cell will flip any pieces, it does so by checking in
        all directions for an opponent piece and if so then it continues in
        that direction until it finds a piece of the current player or an empty
        cell, if it finds a piece of the current player then it will return
        True, otherwise it will return False"""

        # Array of directions to check
        directions = [
            (0, 1),
            (1, 0),
            (0, -1),
            (-1, 0),
            (1, 1),
            (-1, -1),
            (1, -1),
            (-1, 1),
        ]
        # Check if the cell is flippable in any direction
        for dr, dc in directions:
            # Checks if there is an opponent piece in the direction
            r, c = row + dr, col + dc
            if (
                0 <= r < self.board_size
                and 0 <= c < self.board_size
                and self.board[r][c] == self.opponent()
            ):
                """If there is an opponent piece then it will continue in that
                direction until it finds a piece of the current player or an
                empty cell"""
                r, c = r + dr, c + dc
                while 0 <= r < self.board_size and 0 <= c < self.board_size:
                    if self.board[r][c] == self.current_player:
                        return True
                    elif self.board[r][c] == " ":
                        break
                    r, c = r + dr, c + dc
        return False

    def opponent(self):
        """Returns the opposite color of the current player"""
        return "W" if self.current_player == "B" else "B"

    def make_move(self, row, col):
        """Checks if the move is valid, if so then it will place the piece,
        flip the corresponding pieces and update the current player (returns
        True), otherwise it will return False"""

        if self.is_valid_move(row, col):
            self.board[row][col] = self.current_player
            self.flip_pieces(row, col)
            self.current_player = self.opponent()
            return True
        else:
            return False

    def flip_pieces(self, row, col):
        """Flips the pieces in all directions, this is achieved by checking in
        all directions and if there is an opponent piece then it will continue
        in that direction until it finds a piece of the current player or an
        empty cell, if it finds a piece of the current player then it will
        flip all the pieces in that direction."""

        # Array of directions to check
        directions = [
            (0, 1),
            (1, 0),
            (0, -1),
            (-1, 0),
            (1, 1),
            (-1, -1),
            (1, -1),
            (-1, 1),
        ]
        # Similar to is_flippable but it will flip the pieces
        for dr, dc in directions:
            r, c = row + dr, col + dc
            if (
                0 <= r < self.board_size
                and 0 <= c < self.board_size
                and self.board[r][c] == self.opponent()
            ):
                pieces_to_flip = []
                while 0 <= r < self.board_size and 0 <= c < self.board_size:
                    if self.board[r][c] == self.current_player:
                        for flip_r, flip_c in pieces_to_flip:
                            self.board[flip_r][flip_c] = self.current_player
                        break
                    pieces_to_flip.append((r, c))
                    r, c = r + dr, c + dc

    def is_game_over(self):
        """Checks if the game is over, first it checks if there are no more
        empty cells, and then if there are no move valid moves, if any of
        those are true, the game is over"""

        return all(
            all(cell != " " for cell in row) for row in self.board
        ) or not any(self.get_valid_moves())

    def get_valid_moves(self):
        """Returns an array of valid moves, it does so by checking all the
        cells in the board and if the move is valid then it will append it to
        the array.

        TODO: I might implement a help mode that will highlight the valid
        moves.
        """
        valid_moves = []
        for row in range(self.board_size):
            for col in range(self.board_size):
                if self.is_valid_move(row, col):
                    valid_moves.append((row, col))
        return valid_moves

    def get_winner(self):
        """Checks the number of pieces and returns who won or if it's a tie"""

        x_count = sum(row.count("B") for row in self.board)
        o_count = sum(row.count("W") for row in self.board)
        if x_count > o_count:
            return "B"
        elif x_count < o_count:
            return "W"
        else:
            return "Tie"


if __name__ == "__main__":
    root = tk.Tk()
    app = ReversiGUI(root)
    root.mainloop()
