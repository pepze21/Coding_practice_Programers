def search(m, n, board_tf):
    indices = set()
    for i in range(n - 1):
        for j in range(len(board_tf[i]) - 1):
            if j < len(board_tf[i+1]) - 1:
                if board_tf[i][j] == board_tf[i][j+1]:
                    if board_tf[i][j] == board_tf[i+1][j]:
                        if board_tf[i][j] == board_tf[i+1][j+1]:
                            indices.add((i, j))
                            indices.add((i, j+1))
                            indices.add((i+1, j))
                            indices.add((i+1, j+1))
    return indices

def del_shift(m, b, board_tf, indices):
    count = 0
    # 우측부터 pop할 수 있도록, indices를 정렬
    temp = sorted(list(indices), key=(lambda x: x[1]), reverse=True)
    for i, j in temp:
        board_tf[i].pop(j) # delete and shift
        count += 1
    return count

def solution(m, n, board):
    # transpose & flip_horizental & to_list, n * m matrix
    # 우측에서 왼쪽으로 떨어지도록 board를 뒤집고 돌림
    board_tf = [[board[m - i - 1][j] for i in range(m)] for j in range(n)]
    
    indices = set()
    count = 0
    while True:
        indices = search(m, n, board_tf)
        if not indices:
            break
        count += del_shift(m, n, board_tf, indices)
    
    return count