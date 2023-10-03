import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
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
        # Set the background color of the root window
        self.root.configure(bg=BLACK)
        self.game = ReversiGame()

        self.canvas = tk.Canvas(root, width=400, height=400, bg=BLACK)
        self.canvas.pack()

        self.draw_board()
        self.canvas.bind("<Button-1>", self.handle_click)

        self.current_player_label = tk.Label(
            root, text="Current Player: White", bg=BLACK, fg=WHITE
        )

        self.current_player_label.pack()

        self.restart_button = tk.Button(
            root, text="Restart Game", command=self.restart_game,
            bg=BLACK, fg=WHITE, activebackground=LAVANDA, borderwidth=0
        )
        self.restart_button.pack()

        self.root.protocol("WM_DELETE_WINDOW", self.confirm_quit)

    def custom_message_box(self, title, message):
        # Create a new top-level window
        custom_box = tk.Toplevel()

        # Set the window title
        custom_box.title(title)

        # Create a label with the message
        label = tk.Label(custom_box, text=message, fg=WHITE, bg=BLACK)
        label.pack(padx=20, pady=20)

        # Create 'Yes' and 'No' buttons
        def yes_action():
            custom_box.user_response = "yes"
            custom_box.destroy()

        def no_action():
            custom_box.user_response = "no"
            custom_box.destroy()

        yes_button = tk.Button(custom_box, text="Yes",
                               bg=BLACK, fg=WHITE, command=yes_action)
        no_button = tk.Button(custom_box, text="No",
                              bg=BLACK, fg=WHITE, command=no_action)

        # Pack the buttons
        yes_button.pack(side=tk.LEFT, padx=10)
        no_button.pack(side=tk.RIGHT, padx=10)

        # Initialize user_response to None
        custom_box.user_response = None

        # Get the parent window's geometry
        parent_x = self.root.winfo_rootx()
        parent_y = self.root.winfo_rooty()
        parent_width = self.root.winfo_width()
        parent_height = self.root.winfo_height()

        # make it centered
        custom_box_y = parent_y + parent_height // 4
        custom_box_x = parent_x + parent_width // 8
        # Set the new window's geometry
        custom_box.geometry(f"+{custom_box_x}+{custom_box_y}")

        # Wait for the window to be closed
        custom_box.wait_window(custom_box)

        # Return the user's response
        return custom_box.user_response

    def restart_game(self):
        """Reset the game state and redraw the board"""
        user_response = self.custom_message_box(
            "Restart Confirmation", "Are you sure you want to restart the game?"
        )
        if user_response == "yes":
            self.game = ReversiGame()
            self.draw_board()
            self.current_player_label.config(text="Current Player: White")

    def confirm_quit(self):
        """Display a confirmation dialog when leaving the game"""
        user_response = self.custom_message_box(
            "Quit Confirmation", "Are you sure you want to leave the game?"
        )
        if user_response == "yes":
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
        # Count the number of black and white pieces
        black_count = 0
        white_count = 0
        for row in range(self.game.board_size):
            for col in range(self.game.board_size):
                if self.game.board[row][col] == "B":
                    black_count += 1
                elif self.game.board[row][col] == "W":
                    white_count += 1

        if winner == "Tie":
            result = "It's a tie!"
        else:
            result = winner + " wins!"
        result += f" (B:{black_count} - W:{white_count})"
        self.current_player_label.config(text=result)
        self.canvas.unbind("<Button-1>")
