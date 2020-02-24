from random import shuffle
import gtp_connection as gtp


def solve(board, color, pipe):
    """
    Attempts to compute the winner of the current position, assuming perfect play by both, within the current time limit.
    """
    for move in board.get_empty_points():
        if board.is_legal(move,color):
            new_board = board.copy()
            new_board.play_move(move, color)
            if and_node(new_board,gtp.get_opponent_color(color)):
                return pipe.send(move)
    return pipe.send(False)

def and_node(board, color):
    for next_move in board.get_empty_points():
        if board.is_legal(next_move,color):
            new_board = board.copy()
            new_board.play_move(next_move, color)
            if not or_node(new_board,gtp.get_opponent_color(color)):
                return False
    return True

def or_node(board, color):
    for next_move in board.get_empty_points():
        if board.is_legal(next_move,color):
            new_board = board.copy()
            new_board.play_move(next_move, color)
            if and_node(new_board,gtp.get_opponent_color(color)):
                return True
    return False

def doMove(board, move, color):
    board.board[move] = color
    board.current_player = gtp.get_opponent_color(color)

def undoMove(board,move,color):
    board.board[move] = 0
    board.current_player = color