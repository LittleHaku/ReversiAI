"""
File containing the logic implementation of the game
"""


import copy
from random import randint
import time


class ReversiGame:
    """Reversi Game Class"""

    def __init__(self, board=None, current_player=None, move_stack=None):
        """Constructor, initializes the game with a board of 8x8 and the
        initial pieces in the center, also sets the current player to white"""
        self.board_size = 8
        self.board = [
            [" " for _ in range(self.board_size)]
            for _ in range(self.board_size)
        ]

        # Memoization
        self.memoization = {}

        # To compute the average time of the AI
        self.ai_move_times = []

        # To compute the average depth reached
        self.ai_depths = []

        # The AI wont exceed this time for one move
        self.max_time = 1

        # Initial pieces
        if board is None:
            self.board[3][3] = "W"
            self.board[3][4] = "B"
            self.board[4][3] = "B"
            self.board[4][4] = "W"
        else:
            self.board = board

        if current_player is None:
            self.current_player = "W"
        else:
            self.current_player = current_player

        if move_stack is None:
            self.move_stack = [
                ([row[:] for row in self.board], self.current_player)]
        else:
            self.move_stack = move_stack

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

        # print("Move: ", row, col)
        if self.is_valid_move(row, col):
            # print("Valid Move")
            self.board[row][col] = self.current_player
            self.flip_pieces(row, col)
            self.current_player = self.opponent()
            # After making a move, push the current game state onto the stack

            # print("pushing onto stack")
            self.move_stack.append(([row[:]
                                    for row in self.board],
                                    self.current_player))

            # Print the stack
            """ print("Stack: ")
            for state in self.move_stack:
                for row in state[0]:
                    print(row)
                print(state[1]) """
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

    def alphabeta_minimax(self, depth, maximizing_player, alpha, beta,
                          start_time=time.time(), valid_moves=None):
        """ Minimax that will create a new game based on the current game and
        simulate the outcomes of the move there, then return the evaluation
        of the move and a tuple with the move, now with alpha-beta pruning!"""

        # Check time
        if time.time() - start_time > self.max_time:
            raise TimeoutError

        # If the game is over or the depth is 0 then return the evaluation
        if self.is_game_over() or depth == 0:
            evaluation = self.evaluate_board()
            return evaluation, None

        """The first time we call it we will give the valid moves sorted by
        mobility but we cant pass this to the next minimax because since
        there has been another piece placed, the set of valid moves will
        be different"""

        if valid_moves is None:
            valid_moves = self.get_valid_moves()

        # Trying different ways for the memoization
        key = (tuple(tuple(row)
               for row in self.board), self.current_player, depth)

        if key in self.memoization:
            # print("Memoization", self.current_player, depth)
            # return self.memoization[key]
            # Set it as the first in valid moves
            move = self.memoization[key][1]
            # Print before
            # print("Before: ", valid_moves)
            valid_moves.remove(move)
            valid_moves.insert(0, move)
            # print("After: ", valid_moves)

        if maximizing_player:
            max_eval = float("-inf")
            best_move = None

            for move in valid_moves:
                row, col = move
                self.make_move(row, col)
                try:
                    evaluation, _ = self.alphabeta_minimax(
                        depth - 1, False, alpha, beta, start_time)
                except TimeoutError:
                    self.undo_move()
                    raise TimeoutError
                    break
                self.undo_move()

                if evaluation > max_eval:
                    max_eval = evaluation
                    best_move = move

                alpha = max(alpha, evaluation)
                if beta <= alpha:
                    break

            self.memoization[key] = (max_eval, best_move)
            return max_eval, best_move

        else:
            min_eval = float('inf')
            best_move = None

            for move in valid_moves:
                row, col = move
                self.make_move(row, col)
                try:
                    evaluation, _ = self.alphabeta_minimax(
                        depth - 1, True, alpha, beta, start_time)
                except TimeoutError:
                    self.undo_move()
                    raise TimeoutError
                    break
                self.undo_move()

                if evaluation < min_eval:
                    min_eval = evaluation
                    best_move = move

                beta = min(beta, evaluation)
                if beta <= alpha:
                    break

            self.memoization[key] = (min_eval, best_move)
            return min_eval, best_move

    def evaluate_board(self):
        """Simple evaluation function: difference in piece count"""

        # Weights for the evaluation function
        # The weights will be divided into early, mid and late game
        n_pieces = sum(row.count("B") for row in self.board) + \
            sum(row.count("W") for row in self.board)

        if n_pieces < 20:
            # Early game, we dont need to maximize the pieces but the strategy
            # getting a lot of mobility to be able to make better moves
            coin_diff = 10
            coin_placement = 30
            mobility = 50
            frontier = 40
            stability = 10
            corners = 50
        elif n_pieces < 40:
            # Mid game, we need to get the corners and the best spots
            coin_diff = 20
            coin_placement = 70
            mobility = 30
            frontier = 20
            stability = 40
            corners = 70
        else:
            # At this point the game is almost over, we need a lot of pieces
            # and not to get flipped
            coin_diff = 100
            coin_placement = 40
            mobility = 20
            frontier = 10
            stability = 100
            corners = 50

        """ coin_diff = 1
        coin_placement = 50
        mobility = 1
        frontier = 10
        stability = 25
        corners = 50 """

        coin_diff *= self.eval_coin_diff()
        coin_placement *= self.eval_coin_placement()
        mobility *= self.eval_mobility()
        frontier *= self.eval_frontier()
        stability *= self.eval_stability()
        corners *= self.eval_corner()
        """ print("-"*10)

        print("Coin Diff: ", coin_diff)
        print("Coin Placement: ", coin_placement)
        print("Mobility: ", mobility)
        print("Frontier: ", frontier)
        print("Stability: ", stability)
        print("Corners: ", corners) """

        heuristic = coin_diff + coin_placement + mobility + frontier + \
            stability + corners

        return heuristic

    def eval_corner(self):
        """Checks if we have a corner since they are overpowered"""

        # Use opponent for the curr player because have already been swaped
        current = self.opponent()
        opponent = self.current_player

        # Check if the corners are taken
        corners = [(0, 0), (0, 7), (7, 0), (7, 7)]
        current_corners = 0
        opponent_corners = 0
        for corner in corners:
            if self.board[corner[0]][corner[1]] == current:
                current_corners += 1
            elif self.board[corner[0]][corner[1]] == opponent:
                opponent_corners += 1

        difference = current_corners - opponent_corners
        # Normalize
        if current_corners + opponent_corners != 0:
            difference = difference / (current_corners + opponent_corners)
        else:
            difference = 0

        return difference

    def eval_frontier(self):
        """Checks the frontier of the current board, the frontier is the
        empty cells next to a piece, in this case we want to maximize the
        frontier for our player and minimize it for the opponent"""

        # Use opponent for the curr player because have already been swaped
        current = self.opponent()
        opponent = self.current_player
        # Add all the frontier cells to a set to avoid duplicates
        current_frontier = set()
        opponent_frontier = set()

        # Go throught the board
        for row in range(self.board_size):
            for col in range(self.board_size):
                if self.board[row][col] == current:
                    # Get the frontier cells around it
                    frontiers = self.get_frontier(row, col)
                    # Add them to the set
                    current_frontier.update(frontiers)

                elif self.board[row][col] == opponent:
                    # Get the frontier cells around it
                    frontiers = self.get_frontier(row, col)
                    # Add them to the set
                    opponent_frontier.update(frontiers)

        difference = len(current_frontier) - len(opponent_frontier)

        # Normalize the difference to be between -1 and 1
        if len(current_frontier) + len(opponent_frontier) != 0:
            difference = difference / (len(current_frontier) +
                                       len(opponent_frontier))
        else:
            difference = 0

        return difference

    def get_frontier(self, row, col):
        """From the given cell checks in all directions for empty cells,
        if found, they will be returned as frontiers"""

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
        frontiers = []
        for dir_row, dir_col in directions:
            # Checks if there is an empty cell in the direction
            r, c = row + dir_row, col + dir_col
            if (
                0 <= r < self.board_size
                and 0 <= c < self.board_size
                and self.board[r][c] == " "
            ):
                # If there is an empty cell then it will add it to the list
                frontiers.append((r, c))

        return frontiers

    def eval_coin_diff(self):
        """Returns the difference in pieces between the current player and the
        opponent"""
        # Use opponent() for the current player because they have already been
        # swapped
        my_pieces = sum(row.count(self.opponent()) for row in self.board)
        opponent_pieces = sum(row.count(self.current_player)
                              for row in self.board)

        difference = my_pieces - opponent_pieces

        # Normalize the difference to be between -1 and 1
        if my_pieces + opponent_pieces != 0:
            difference = difference / (my_pieces + opponent_pieces)
        else:
            difference = 0

        return difference

    def eval_coin_placement(self):
        """Checks if the coins are in a good position or not, the corners are
        the best positions, thus, we penalize the coins that could give them
        away, also the edges are good places and the center not that good
        """

        board = [[100, -20, 10, 5, 5, 10, -20, 100],
                 [-20, -50, -2, -2, -2, -2, -50, -20],
                 [10, -2, -1, -1, -1, -1, -2, 10],
                 [5, -2, -1, -1, -1, -1, -2, 5],
                 [5, -2, -1, -1, -1, -1, -2, 5],
                 [10, -2, -1, -1, -1, -1, -2, 10],
                 [-20, -50, -2, -2, -2, -2, -50, -20],
                 [100, -20, 10, 5, 5, 10, -20, 100]]

        # Use opponent for the curr player because have already been swaped
        current = self.opponent()
        opponent = self.current_player
        curr_sum = 0
        opp_sum = 0
        for row in range(self.board_size):
            for col in range(self.board_size):
                if self.board[row][col] == current:
                    curr_sum += board[row][col]
                elif self.board[row][col] == opponent:
                    opp_sum += board[row][col]

        difference = curr_sum - opp_sum

        max_sum = abs(opp_sum) + abs(curr_sum)

        if max_sum != 0:
            difference = difference / max_sum
        else:
            difference = 0

        # Print board
        """ for row in self.board:
            print(row) """

        return difference

    def eval_mobility(self):
        """Checks the number of moves for each player to limit the opponent's
        moves and increase the player's moves"""

        # Use opponent for the curr player because have already been swaped
        current = self.opponent()
        current_moves = len(self.get_valid_moves())
        self.current_player = current
        opponent_moves = len(self.get_valid_moves())
        self.current_player = self.opponent()

        difference = current_moves - opponent_moves

        # Normalize
        if current_moves + opponent_moves != 0:
            difference = difference / (current_moves + opponent_moves)
        else:
            difference = 0

        return difference

    def eval_stability(self):
        """Checks the number of pieces that can't be flipped, the more the
        better"""

        # Use opponent for the curr player because have already been swaped
        current = self.opponent()
        opponent = self.current_player
        current_stability = self.get_stability(current)
        opponent_stability = self.get_stability(opponent)

        difference = current_stability - opponent_stability

        # Normalize
        if current_stability + opponent_stability != 0:
            difference = difference / (current_stability + opponent_stability)
        else:
            difference = 0

        return difference

    def get_stability(self, player):
        """Checks the number of pieces that can't be flipped for the given
        player"""

        # Add all the stable cells to a set to avoid duplicates
        stable_cells = set()

        # Go throught the board
        for row in range(self.board_size):
            for col in range(self.board_size):
                if self.board[row][col] == player:
                    # Check if it's stable
                    if self.is_stable(row, col):
                        # Add it to the set
                        stable_cells.add((row, col))

        return len(stable_cells)

    def is_stable(self, row, col):
        """Similar to is_flippable but it will check if the cell is stable"""

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

        # Get the player in the cell
        player = self.board[row][col]
        if player == "B":
            opponent = "W"
        else:
            opponent = "B"

        # Check if it can be flipped in any direction
        for dr, dc in directions:
            # Checks if there is an opponent piece in the direction
            r, c = row + dr, col + dc
            if (
                0 <= r < self.board_size
                and 0 <= c < self.board_size
                and self.board[r][c] == opponent
            ):
                """If there is an opponent piece then it will continue in that
                direction until it finds a piece of the current player or an
                empty cell"""
                r, c = r + dr, c + dc
                while 0 <= r < self.board_size and 0 <= c < self.board_size:
                    if self.board[r][c] == player:
                        return True
                    elif self.board[r][c] == " ":
                        break
                    r, c = r + dr, c + dc
        return True

    def undo_move(self):
        """Undo the move by popping the previous game state from the stack"""
        # If we take the top we get the current game state, so we pop the top
        # and get the top one
        """ print("Undoing Move")
        print("Stack before pop: ")
        for state in self.move_stack:
            for row in state[0]:
                print(row)
            print(state[1])
            print("-"*10) """

        self.move_stack.pop()
        # Get the last element of the stack
        # But important GET A COPY!!!
        last_state = self.move_stack[-1]
        self.board = copy.deepcopy(last_state[0])
        self.current_player = last_state[1]

        # Print the board after undoing the move
        """ print("Undo Move: ")
        for row in self.board:
            print(row)
        print("Current Player: ", self.current_player)
        print("-"*10) """

        # Print the stack
        """ print("Stack after pop: ")
        for state in self.move_stack:
            for row in state[0]:
                print(row)
            print(state[1])
            print("-"*10) """

    def first_ai_move(self):
        """Make a random move for the first move"""
        valid_moves = self.get_valid_moves()
        # select a random move
        n_moves = len(valid_moves)
        random = randint(0, n_moves - 1)
        move = valid_moves[random]

        row, col = move
        self.make_move(row, col)

    def ai_move(self):
        """Makes a move using the minimax algorithm"""

        start_time = time.time()
        max_depth = 10
        alpha = float("-inf")
        beta = float("inf")
        best_move = None
        stating_depth = 2

        valid_moves = self.get_valid_moves()

        for depth in range(stating_depth, max_depth + 1):
            # Check if the max time has passed
            if time.time() - start_time >= self.max_time:
                break

            move = None

            try:
                if depth % 2 == 0:
                    _, move = self.alphabeta_minimax(
                        depth, False, alpha, beta, start_time, valid_moves)
                else:
                    _, move = self.alphabeta_minimax(
                        depth, True, alpha, beta, start_time, valid_moves)

                if move is not None:
                    best_move = move
            except TimeoutError:
                # Decrease one because it wasnt trully evaluated
                depth -= 1
                break

        self.ai_move_times.append(time.time() - start_time)
        self.ai_depths.append(depth)
        print("AI Move: ", best_move)
        print("-"*10)
        print("Move Time: ", time.time() - start_time)
        print("Depth: ", depth)
        row, col = best_move

        self.make_move(row, col)
