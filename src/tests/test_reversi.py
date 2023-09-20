"""
Module to test out the ReversiGame class
"""
import unittest
from reversi.reversi_logic import ReversiGame


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

    
if __name__ == '__main__':
    unittest.main()
