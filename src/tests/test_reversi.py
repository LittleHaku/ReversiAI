"""
Module to test out the ReversiGame class
"""
import copy
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

    def test_create_game_from_started(self):
        # Test to create a new ReverseGame from a started game
        # Create a new game
        new_game = ReversiGame()
        # Make a move
        new_game.make_move(2, 4)
        # save board, player and stack
        board = copy.deepcopy(new_game.board)
        current_player = new_game.current_player
        stack = copy.deepcopy(new_game.move_stack)

        # Create a new game from the started game
        new_game = ReversiGame(board, current_player, stack)
        # Check the board is the same
        self.assertEqual(new_game.board, board)
        # Check the current player is the same
        self.assertEqual(new_game.current_player, 'B')
        # Check the stack is the same
        self.assertEqual(new_game.move_stack, stack)

    def test_alpha_beta_minimax_ai_win(self):
        # Create a board where the AI (blacks) can win with one move
        board = [
            ['B', 'W', 'B', 'B', 'B', 'B', 'W', ' '],
            ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],
            ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],
            ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],
            ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],
            ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],
            ['B', 'B', 'B', 'B', 'W', 'B', 'B', 'B'],
            ['B', 'B', 'B', 'B', ' ', 'B', 'B', 'B']
        ]
        current_player = 'B'

        game = ReversiGame(board, current_player)

        depth = 3
        alpha = float("-inf")
        beta = float("inf")
        eval, move = game.alphabeta_minimax(
            depth, True, alpha, beta)

        print(eval)
        print(move)

        self.assertGreaterEqual(eval, 50)
        self.assertEqual(move, (0, 7))

    def test_alpha_beta_minimax_ai_loses(self):
        # Create a board where the AI (blacks) will lose
        board = [
            ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
            ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
            ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
            ['B', 'B', 'W', 'W', 'W', 'W', 'W', 'W'],
            ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
            ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
            [' ', ' ', 'W', 'W', 'W', 'W', 'W', 'W'],
            [' ', ' ', 'W', 'W', 'W', 'W', 'W', 'W']
        ]
        current_player = 'B'
        game = ReversiGame(board, current_player)

        depth = 3
        alpha = float("-inf")
        beta = float("inf")
        eval, move = game.alphabeta_minimax(
            depth, True, alpha, beta)

        print(eval)
        print(move)
        self.assertLessEqual(eval, -50)

    def test_ai_move(self):
        # Create a board where the AI (blacks) can win with one move
        board = [
            ['B', 'W', 'B', 'B', 'B', 'B', 'W', ' '],
            ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],
            ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],
            ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],
            ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],
            ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],
            ['B', 'B', 'B', 'B', 'W', 'B', 'B', 'B'],
            ['B', 'B', 'B', 'B', ' ', 'B', 'B', 'B']
        ]
        expected_board = [
            ['B', 'W', 'B', 'B', 'B', 'B', 'B', 'B'],
            ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],
            ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],
            ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],
            ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],
            ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],
            ['B', 'B', 'B', 'B', 'W', 'B', 'B', 'B'],
            ['B', 'B', 'B', 'B', ' ', 'B', 'B', 'B']
        ]
        current_player = 'B'

        game = ReversiGame(board, current_player)
        game.ai_move()

        self.assertEqual(game.board, expected_board)

    def test_pruning(self):
        # Create a normal game, make a move and let them play
        game = ReversiGame()
        # Make a move at (5, 2)
        game.make_move(5, 2)
        # Let AI execute
        game.ai_move()

    def test_eval_coin_placement(self):
        # Create a board with known evaluation
        board = [
            ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],
            ['W', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['W', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['W', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        ]

        current_player = 'W'

        game = ReversiGame(board, current_player)

        # We know the sum of the game will be
        # 100 -20 +10 +5 +5 +10 -20 +100 = 190 black
        # -20 + 10 +5 = -5 white
        # the difference will be 195
        # when normalized it will be 1
        self.assertEqual(game.eval_coin_placement(), 1)

    def test_eval_coin_placement_divide_zero(self):
        # Create a board where the evaluation will be divided by zero
        board = [
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        ]

        current_player = 'W'

        game = ReversiGame(board, current_player)

        # Both player have the same placement so the evaluation will be 0
        self.assertEqual(game.eval_coin_placement(), 0)

    def test_eval_corners_divide_zero(self):
        # Board the sum of corners will be divided by zero
        board = [
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', 'W', 'B', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        ]

        current_player = 'W'

        game = ReversiGame(board, current_player)

        # Both player have the same number of corners so the evaluation
        # will be 0
        self.assertEqual(game.eval_corner(), 0)

    def test_eval_frontier_divide_zero(self):
        # Board where the sum of frontiers must be divided b zero
        # apart from the empty board i dont think any other board meets this
        board = [
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        ]

        current_player = 'W'

        game = ReversiGame(board, current_player)

        # Both player have the same number of frontiers so the evaluation
        # will be 0
        self.assertEqual(game.eval_frontier(), 0)

    def test_eval_coin_diff_divide_zero(self):
        # Board where the sum of coins must be zero
        # Once again i dont think any other board meets this
        board = [
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        ]
        current_player = 'W'

        game = ReversiGame(board, current_player)

        self.assertEqual(game.eval_coin_diff(), 0)

    def test_eval_mobility_divide_zero(self):
        # board where none has mobility
        # this would mean the game is over but just in case
        # i added the condition
        board = [
            ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],
            ['B', 'W', 'W', 'W', 'W', 'W', 'W', 'B'],
            ['B', 'W', 'W', 'W', 'W', 'W', 'W', 'B'],
            ['B', 'W', 'W', 'W', 'W', 'W', 'W', 'B'],
            ['B', 'W', 'W', 'W', 'W', 'W', 'W', 'B'],
            ['B', 'W', 'W', 'W', 'W', 'W', 'W', 'B'],
            ['B', 'W', 'W', 'W', 'W', 'W', 'W', 'B'],
            ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B']
        ]

        current_player = 'W'
        game = ReversiGame(board, current_player)

        self.assertEqual(game.eval_mobility(), 0)

    def test_eval_stability_divide_zero(self):
        # board where none has stability
        # i cant think of any other board other than the empty one

        board = [
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        ]

        current_player = 'W'
        game = ReversiGame(board, current_player)

        self.assertEqual(game.eval_stability(), 0)

    def test_mid_game(self):
        # Test it makes correct moves in a mid game scenario
        # Board with 20 < coins < 40
        board = [
            ['B', 'W', 'B', 'B', 'B', 'B', 'W', ' '],
            ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],
            ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],
            ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        ]
        expected_board = [
            ['B', 'W', 'B', 'B', 'B', 'B', 'B', 'B'],
            ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],
            ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],
            ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        ]

        current_player = 'B'

        game = ReversiGame(board, current_player)
        game.ai_move()
        self.assertEqual(game.board, expected_board)

    def test_first_random_ai_move(self):
        game = ReversiGame()
        game.first_ai_move()

        possible_moves = [(2, 4), (3, 5), (4, 2), (5, 3)]
        # Check only one of these cells has now a white piece
        white_pieces = [game.board[i][j] == 'W' for i, j in possible_moves]
        self.assertEqual(white_pieces.count(True), 1)


if __name__ == '__main__':
    unittest.main()
