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
        """Create a custom message box with a black background and white text"""
        root = tk.Tk()
        root.withdraw()

        # Create a custom Toplevel widget with a black background
        top = tk.Toplevel(root, bg=BLACK)
        top.title(title)

        # Create a Label widget with the message text and white text color
        message_label = tk.Label(
            top, text=message, bg=BLACK, fg=WHITE, font=("TkDefaultFont", 12)
        )
        message_label.pack(padx=20, pady=20)

        # Create a Frame widget to hold the buttons
        button_frame = tk.Frame(top, bg=BLACK)
        button_frame.pack(padx=20, pady=10)

        # Create a custom Button widget with a black background and white text color
        ok_button = tk.Button(
            button_frame,
            text="OK",
            command=top.destroy,
            bg=BLACK,
            fg=WHITE,
            font=("TkDefaultFont", 12),
            borderwidth=0,
            activebackground=LAVANDA,
        )
        ok_button.pack(side="left", padx=10)

        # Create a custom Button widget with a black background and white text color
        cancel_button = tk.Button(
            button_frame,
            text="Cancel",
            command=top.destroy,
            bg=BLACK,
            fg=WHITE,
            font=("TkDefaultFont", 12),
            borderwidth=0,
            activebackground=LAVANDA,
        )
        cancel_button.pack(side="left", padx=10)

        # Center the Toplevel widget on the screen
        top.update_idletasks()
        width = top.winfo_width()
        height = top.winfo_height()
        x = (top.winfo_screenwidth() // 2) - (width // 2)
        y = (top.winfo_screenheight() // 2) - (height // 2)
        top.geometry("{}x{}+{}+{}".format(width, height, x, y))

        # Make the Toplevel widget modal
        top.grab_set()
        top.wait_window()

        return "yes"

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
