def solve(board, color, pipe):
    global index_map, exp3, ttable
    ttable ={}
    exp3 = {i:0 for i in range(0,3*board.size**2,3)}
    for i in range(1,3*board.size**2,3):
        exp3[i] = 3**i
        exp3[i+1] = exp3[i]<<1
    index_map = {i + 1 + (board.size+1)*(j + 1): 3*(board.size*j+i) for j in range(board.size) for i in range(board.size)}
    board.base3int = int(sum(exp3[index_map[i]+color] for i,color in enumerate(board.board) if color != 3))
    return pipe.send(negamax(board, color))

def negamax(board,color):
    result = ttable.get(board.base3int, None)
    if result != None:
        return result
    for next_move in board.get_empty_points():
        if is_legal(board, next_move, color):
            next_player = 3 - color
            prev_int = board.base3int

            board.board[next_move] = color
            board.current_player = next_player
            board.base3int += exp3[index_map[next_move]+color]

            success = not negamax(board, next_player)

            board.board[next_move] = 0
            board.current_player = color
            board.base3int = prev_int

            if success:
                ttable[board.base3int] = next_move
                return next_move
    ttable[board.base3int] = False
    return False

def is_legal(board, move, color):
    board.board[move] = color
    try:
        if any(board._detect_and_process_capture(nb) for nb in board.neighbors[move] if board.board[nb] == 3 - color):
            raise
        if not board._stone_has_liberty(move) and not board._has_liberty(board._block_of(move)):
            raise
    except:
        return False
    else:
        return True
    finally:
        board.board[move] = 0
