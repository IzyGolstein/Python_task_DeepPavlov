def initialize_board(n, m):
    return [[-1 for _ in range(m)] for _ in range(n)]

move = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]

def get_valid_moves(board, i, j, n, m):
    valid_moves = []
    for mi, mj in move:
        i_new = i + mi
        j_new = j + mj

        if 0 <= i_new < m and 0 <= j_new < n and board[i_new][j_new] == -1:
            valid_moves.append((i_new, j_new))
    return valid_moves

def push_to_stack(i, j, pos, stack, board):
    board[i][j] = pos
    stack.append((i, j, pos))

def pop_from_stack(stack, board):
    i, j, pos = stack.pop()
    board[i][j] = -1
    return i, j, pos

def get_knight_path(m, n):
    a = initialize_board(m, n)
    stack = []

    for i in range(m):
        for j in range(n):
            push_to_stack(i, j, 1, stack, a)

            while stack:
                i, j, pos = stack[-1]

                if pos == n * m:
                    return a

                valid_moves = get_valid_moves(a, i, j, n, m)

                if not valid_moves:
                    pop_from_stack(stack, a)
                    continue

                valid_moves.sort(key=lambda move: len(get_valid_moves(a, move[0], move[1], n, m)))

                for i_new, j_new in valid_moves:
                    push_to_stack(i_new, j_new, pos + 1, stack, a)
                    break
                else:
                    pop_from_stack(stack, a)

    return []

def convert_path_to_coordinates(path, m, n):
    coordinates = []
    for i in range(1, n * m + 1):
        for row in range(m):
            for col in range(n):
                if path[row][col] == i:
                    coordinates.append([row, col])
    return coordinates

def main(size):
    m, n = size
    knight_path = get_knight_path(m, n)
    return convert_path_to_coordinates(knight_path, m, n)

# %%
