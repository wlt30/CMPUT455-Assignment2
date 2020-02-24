from random import shuffle

def solve(board, color, pipe):
    """
    Attempts to compute the winner of the current position, assuming perfect play by both, within the current time limit.
    """
    for move in board.get_empty_points():
        if board.is_legal(move,color):
            if and_node(board,color,move):
                return pipe.send(move)

def and_node(board, color, move):
    new_board=board[:]
    new_board.play_move(move, color)
    for move in board.get_empty_points():
        if board.is_legal(move,color):
            if not or_node(board,color,move):
                return False
    return move
    # return all(or_node(new_board,color,move) for move in new_board.get_empty_points() if new_board.is_legal(move,color))

def or_node(board, color, move=False):
    if move:
        new_board=board[:]
        new_board.play_move(move, color)
    for move in board.get_empty_points():
        if board.is_legal(move,color):
            if and_node(board,color,move):
                return move
    return False
    # return any(and_node(new_board,color,move) for move in new_board.get_empty_points() if new_board.is_legal(move,color))
