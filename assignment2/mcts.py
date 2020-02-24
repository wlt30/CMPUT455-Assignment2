from random import shuffle
import gtp_connection as gtp

ttable ={}
def solve(board, color, pipe):
    """
    Attempts to compute the winner of the current position, assuming perfect play by both, within the current time limit.
    """
    # print(hash(str(board.board)))
    for next_move in board.get_empty_points():
        if board.is_legal(next_move,color):
            doMove(board, next_move, color)
            is_win = and_node(board,3-color)
            undoMove(board, next_move, color)
            if is_win:
                return pipe.send(next_move)
    return pipe.send(False)

def and_node(board, color):
    board_repr = str(board.board)
    result = ttable.get(board_repr, None)
    if result != None:
        return result
        
    for next_move in board.get_empty_points():
        if board.is_legal(next_move,color):
            doMove(board, next_move, color)
            is_loss = not or_node(board,3-color)
            undoMove(board, next_move, color)
            if is_loss:
                ttable[str(board.board)] = False
                return False
    ttable[board_repr]=True
    return True

def or_node(board, color):
    board_repr = str(board.board)
    result = ttable.get(board_repr, None)
    if result != None:
        return result

    for next_move in board.get_empty_points():
        if board.is_legal(next_move,color):
            doMove(board, next_move, color)
            is_win = and_node(board, 3-color)
            undoMove(board, next_move, color)
            if is_win:
                ttable[str(board.board)]=True
                return True
    ttable[board_repr]=False
    return False

def doMove(board, move, color):
    board.board[move] = color
    board.current_player = 3-color

def undoMove(board,move,color):
    board.board[move] = 0
    board.current_player = color