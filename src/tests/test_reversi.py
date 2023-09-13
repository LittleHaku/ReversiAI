"""
Module to test out the ReversiGame class
"""
from tkinter import Tk, messagebox
import unittest
from reversi.reversi import ReversiGame, ReversiGUI
from unittest import mock


class TestReversiGame(unittest.TestCase):

    def setUp(self):
        # Create a new instance of ReversiGame for each test case
        self.game = ReversiGame()

    def test_initial_board_setup(self):
        # Test that the initial board setup is correct
        expected_board = [
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', 'W', 'B', ' ', ' ', ' '],
            [' ', ' ', ' ', 'B', 'W', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        ]
        self.assertEqual(self.game.board, expected_board)
        self.assertEqual(self.game.current_player, 'W')

    def test_valid_moves(self):
        # Test the get_valid_moves method
        valid_moves = self.game.get_valid_moves()

        # Since the game starts with the white player, the valid moves are:
        expected_valid_moves = [(2, 4), (3, 5), (4, 2), (5, 3)]

        # (order doesn't matter)
        for move in valid_moves:
            self.assertIn(move, expected_valid_moves)

    def test_make_move(self):
        # Test the make_move method
        # First with a valid move
        self.assertTrue(self.game.make_move(2, 4))
        # Check the piece is placed
        self.assertEqual(self.game.board[2][4], 'W')

        # Then with an invalid move (already occupied cell)
        self.assertFalse(self.game.make_move(2, 4))
        # Check the board is not modified
        self.assertEqual(self.game.board[2][4], 'W')

    def test_winner(self):
        # Test the get_winner method for black winning
        self.game.board = [
            ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],
            ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],
            ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],
            ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],
            ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],
            ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],
            ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],
            ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B']
        ]
        self.assertEqual(self.game.get_winner(), 'B')
        # Test it for white winning
        self.game.board = [
            ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
            ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
            ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
            ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
            ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
            ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
            ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
            ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W']
        ]
        self.assertEqual(self.game.get_winner(), 'W')
        # Test it for a tie
        self.game.board = [
            ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],
            ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],
            ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],
            ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],
            ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
            ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
            ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
            ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W']
        ]
        self.assertEqual(self.game.get_winner(), 'Tie')

    def test_is_game_over(self):
        # Test the is_game_over method
        self.assertFalse(self.game.is_game_over())
        self.game.board = [
            ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
            ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
            ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
            ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
            ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
            ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
            ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
            ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W']
        ]
        self.assertTrue(self.game.is_game_over())


class TestReversiGUI(unittest.TestCase):
    def setUp(self):
        self.root = Tk()
        self.app = ReversiGUI(self.root)

    def tearDown(self):
        self.root.destroy()

    def test_gui_initialization(self):
        # Check the title
        self.assertEqual(self.app.root.title(), "Reversi Game")
        # Check labels
        self.assertEqual(
            self.app.current_player_label["text"], "Current Player: White")

    def test_handle_click_initial_board(self):
        # Test the handle_click method
        # First with a valid move
        self.app.game = ReversiGame()

        # (4, 2) would be a valid move for the initial board setup
        # Each cell is 50x50 pixels, so we click in the middle of the cell
        x = 4 * 50 + 25
        y = 2 * 50 + 25
        # First lets check that the cell is empty
        self.assertEqual(self.app.game.board[2][4], ' ')
        # Create the event object
        event = mock.Mock(x=x, y=y)

        self.app.handle_click(event)

        self.assertEqual(self.app.game.board[2][4], 'W')

        # Then with an invalid move (already occupied cell)
        self.app.handle_click(mock.Mock(x=x, y=y))
        self.assertEqual(self.app.game.board[2][4], 'W')

        # Then with a valid move for black
        self.app.handle_click(mock.Mock(x=3 * 50 + 25, y=2 * 50 + 25))
        self.assertEqual(self.app.game.board[2][3], 'B')

    def test_handle_click_game_over_black_wins(self):
        # Test the handle_click method when the game is over
        self.app.game = ReversiGame()
        # Set the board to the final move
        self.app.game.board = [
            ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'W'],
            ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],
            ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],
            ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],
            ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],
            ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],
            ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],
            ['B', 'B', 'B', 'B', 'B', 'B', 'B', ' ']
        ]

        # Create the event object for the bottom right cell
        event = mock.Mock(x=7 * 50 + 25, y=7 * 50 + 25)

        self.app.handle_click(event)
        # Check that the label is updated with the winner
        self.assertEqual(self.app.current_player_label["text"], "B wins!")

    def test_handle_click_game_over_tie(self):
        # Test the handle_click method when the game is over
        self.app.game = ReversiGame()
        # Set the board to the final move
        self.app.game.board = [
            ['B', 'B', 'B', 'B', 'W', 'W', 'W', 'W'],
            ['B', 'B', 'B', 'B', 'W', 'W', 'W', 'W'],
            ['B', 'B', 'B', 'B', 'W', 'W', 'W', 'W'],
            ['B', 'B', 'B', 'B', 'W', 'W', 'W', 'W'],
            ['B', 'B', 'B', 'B', 'W', 'W', 'W', 'W'],
            ['B', 'B', 'B', 'B', 'W', 'W', 'W', 'W'],
            ['B', 'B', 'B', 'B', 'W', 'W', 'W', 'B'],
            ['B', 'B', 'B', 'B', 'W', 'W', 'W', ' ']
        ]

        # Create the event object for the bottom right cell
        event = mock.Mock(x=7 * 50 + 25, y=7 * 50 + 25)

        self.app.handle_click(event)
        # Check that the label is updated with a tie
        self.assertEqual(self.app.current_player_label["text"], "It's a tie!")

    def test_confirm_quit(self):
        # Test the confirm_quit method
        # First with a negative answer
        with mock.patch.object(messagebox, 'askyesno', return_value=False):
            self.app.confirm_quit()
            # Check that the popup was shown
            self.assertTrue(messagebox.askyesno.called)
            # Check that the root window was not destroyed
            self.assertTrue(self.app.root.winfo_exists())

        # Then with a true answer
        with mock.patch.object(messagebox, 'askyesno', return_value=True):
            self.app.confirm_quit()
            # Check that the popup was shown
            self.assertTrue(messagebox.askyesno.called)


if __name__ == '__main__':
    unittest.main()
