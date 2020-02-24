from random import shuffle
import gtp_connection as gtp
def solve(board, color, pipe):
    """
    Attempts to compute the winner of the current position, assuming perfect play by both, within the current time limit.
    """
    for move in board.get_empty_points():
        if board.is_legal(move,color):
            if and_node(board,gtp.get_opponent_color(color),move):
                print("in mcts: found move")
                return pipe.send(move)
    print("in mcts: did not find move")
    return pipe.send(False)

def and_node(board, color, move):
    new_board = board.copy()
    new_board.play_move(move, color)
    for next_move in new_board.get_empty_points():
        if new_board.is_legal(next_move,color):
            if not or_node(new_board,gtp.get_opponent_color(color),next_move):
                print("and_node: False")
                return False
    print("and_node: move")
    return move
    # return all(or_node(new_board,color,move) for move in new_board.get_empty_points() if new_board.is_legal(move,color))

def or_node(board, color, move):
    new_board = board.copy()
    new_board.play_move(move, color)
    for next_move in new_board.get_empty_points():
        if new_board.is_legal(next_move,color):
            if and_node(new_board,gtp.get_opponent_color(color),next_move):
                print("or_node: move")
                return move
    print("or_node: False")
    return False
    # return any(and_node(new_board,color,move) for move in new_board.get_empty_points() if new_board.is_legal(move,color))
