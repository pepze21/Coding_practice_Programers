def checker(key_phase, lock, N):
    for i in range(N):
        for j in range(N):
            if (key_phase[i][j] + lock[i][j] != 1):
                return False
    return True

def rotation(key, angle): # +90 degree per +1
    M = len(key)
    if (angle % 4) == 1:
        return [[key[i][M-1-j] for i in range(M)] for j in range(M)]
    elif (angle % 4) == 2:
        return [[key[M-1-j][M-1-i] for i in range(M)] for j in range(M)]
    elif (angle % 4) == 3:
        return [[key[M-1-i][j] for i in range(M)] for j in range(M)]
    else:
        return key
    
def para_trans(key, lock, a, b):
    M = len(key)
    N = len(lock)
    para_key = [[0] * N for _ in range(N)]
    
    for i in range(min(a, N) - max(a - M, 0)):
        para_key[max(a - M, 0) : min(a, N)][i][max(b - M, 0) : min(b, N)] = key[max(M - a, 0) : min(M + N - a, M)][i][max(M - b, 0) : min(M + N - b, M)]
    return para_key

def solution(key, lock):
    M = len(key)
    N = len(lock)

    for angle in range(4):
        for i in range(M + N + 1):
            for j in range(M + N + 1):
                key_phase = para_trans(rotation(key, angle), lock, i, j)
                if (checker(key_phase, lock, N)):
                    return True
    return False