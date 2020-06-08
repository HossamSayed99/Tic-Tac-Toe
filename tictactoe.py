"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    """
    Counting the number of X's and O's in a board
    If both are equal, then it is the X's turn
    Else it is the O's turn
    """
    xsPlayed = 0
    osPlayed = 0
    for row in board:
        for cell in row:
            if cell == X:
                xsPlayed += 1
            elif cell == O:
                osPlayed += 1
    if xsPlayed == osPlayed:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    """
    Looping over the board and returning all empty cells
    """
    possibleActions = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possibleActions.add((i, j))
    return possibleActions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    playerToPlay = player(board)
    newboard = copy.deepcopy(board)
    if newboard[action[0]][action[1]] != EMPTY:
        raise ValueError('Invalid action on given board')
    newboard[action[0]][action[1]] = playerToPlay
    return newboard


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        # Check row
        if board[i][0] == X and board[i][1] == X and board[i][2] == X:
            return X
        if board[i][0] == O and board[i][1] == O and board[i][2] == O:
            return O
        # Check column
        if board[0][i] == X and board[1][i] == X and board[2][i] == X:
            return X
        if board[0][i] == O and board[1][i] == O and board[2][i] == O:
            return O
    # Check diagonal
    if board[0][0] == X and board[1][1] == X and board[2][2] == X:
        return X
    if board[0][0] == O and board[1][1] == O and board[2][2] == O:
        return O
    if board[0][2] == X and board[1][1] == X and board[2][0] == X:
        return X
    if board[0][2] == O and board[1][1] == O and board[2][0] == O:
        return O
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None:
        return True
    for row in board:
        for cell in row:
            if cell == EMPTY:
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    playerToWin = winner(board)
    if playerToWin == X:
        return 1
    elif playerToWin == O:
        return -1
    else:
        return 0
    # raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return (None, None)
    # Decining which player should move and which action should be taken
    playerToPlay = player(board)
    possibleActions = actions(board)
    bestAction = None
    mx = -1
    mn = 10000000
    # Looping over all possible actions
    for action in possibleActions:
        resultBoard = result(board, action)
        # if the current action results in a termianl board
        if (terminal(resultBoard)):
            score = utility(resultBoard)
            # If the player is X and this action makes him win, then return it
            if playerToPlay == X:
                if score == 1:
                    return (action, 1)
                elif score > mx:
                    mx = score
                    bestAction = action
            # Same with O
            elif playerToPlay == O:
                if score == -1:
                    return (action, -1)
                elif score < mn:
                    mn = score
                    bestAction = action
        else:
            # if the reusulting board is not a terminal one
            # Then recurse on the board and return its value
            score = minimax(resultBoard)
            if playerToPlay == X:
                if score[1] == 1:
                    return (action, 1)
                elif score[1] > mx:
                    mx = score[1]
                    bestAction = action
            elif playerToPlay == O:
                if score[1] == -1:
                    return (action, -1)
                elif score[1] < mn:
                    mn = score[1]
                    bestAction = action
    # Return tuple of the best action to take and its best score
    if playerToPlay == X:
        return (bestAction, mx)
    else:
        return (bestAction, mn)
