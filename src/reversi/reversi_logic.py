"""
File containing the logic implementation of the game
"""


class ReversiGame:
    """Reversi Game Class"""

    def __init__(self, board=None, current_player=None):
        """Constructor, initializes the game with a board of 8x8 and the
        initial pieces in the center, also sets the current player to white"""
        self.board_size = 8
        self.board = [
            [" " for _ in range(self.board_size)]
            for _ in range(self.board_size)
        ]
        # Initialize an empty stack to store previous game states
        self.move_stack = []
        # Initial pieces
        if board is None and current_player is None:
            self.board[3][3] = "W"
            self.board[3][4] = "B"
            self.board[4][3] = "B"
            self.board[4][4] = "W"
            self.current_player = "W"
        else:
            self.board = board
            self.current_player = current_player

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

        print("Move: ", row, col)
        if self.is_valid_move(row, col):
            # print("Valid Move")
            self.board[row][col] = self.current_player
            self.flip_pieces(row, col)
            self.current_player = self.opponent()
            # After making a move, push the current game state onto the stack
            self.move_stack.append((self.board, self.current_player))
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

    def alphabeta_minimax(self, depth, maximizing_player, alpha, beta):
        """ Minimax that will create a new game based on the current game and
        simulate the outcomes of the move there, then return the evaluation
        of the move and a tuple with the move, now with alpha-beta pruning!"""

        # If the game is over or the depth is 0 then return the evaluation
        if self.is_game_over() or depth == 0:
            return self.evaluate_board(), None

        valid_moves = self.get_valid_moves()

        # If the player is maximizing then it will return the maximum value
        if maximizing_player:
            max_eval = float("-inf")
            best_move = None

            for move in valid_moves:
                row, col = move
                # Make the move
                self.make_move(row, col)
                # Recursively call minimax for the next level
                evaluation, _ = self.alphabeta_minimax(
                    depth - 1, False, alpha, beta)
                # Undo the move
                self.undo_move()

                if evaluation > max_eval:
                    best_eval = evaluation
                    best_move = move

                # Take the better between current eval and current alpha
                alpha = max(alpha, evaluation)

                # If beta is less than or equal to alpha then prune
                if beta <= alpha:
                    break

            return best_eval, best_move

        # If the player is minimizing then it will return the minimum value
        else:
            best_eval = float('inf')
            best_move = None

            for move in valid_moves:
                row, col = move
                # Make the move
                self.make_move(row, col)
                # Recursively call minimax for the next level
                evaluation, _ = self.alphabeta_minimax(
                    depth - 1, True, alpha, beta)
                # Undo the move
                self.undo_move()

                if evaluation < best_eval:
                    best_eval = evaluation
                    best_move = move

                # Take the better between current eval and current beta
                beta = min(beta, evaluation)

                # If beta is less than or equal to alpha then prune
                if beta <= alpha:
                    break

            return best_eval, best_move

    def evaluate_board(self):
        """Simple evaluation function: difference in piece count"""
        ai_pieces = sum(row.count(self.current_player) for row in self.board)
        opponent_pieces = sum(row.count(self.opponent()) for row in self.board)
        return ai_pieces - opponent_pieces

    def undo_move(self):
        """Undo the move by popping the previous game state from the stack"""
        if self.move_stack:
            self.board, self.current_player = self.move_stack.pop()

    def ai_move(self):
        """Makes a move using the minimax algorithm"""

        # Make a copy of the state of the game
        # Make a copy of the board because if not it places two pieces
        game_copy = ReversiGame([row[:]
                                for row in self.board], self.current_player)

        _, move = game_copy.alphabeta_minimax(
            3, True, float("-inf"), float("inf"))
        print("AI Move: ", move)
        row, col = move
        # print("AI Move: ", row, col)

        self.make_move(row, col)
