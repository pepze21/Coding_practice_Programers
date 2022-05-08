def solution(arr):
    m = len(arr)
    ones = sum(map(sum, arr))
    answer = [m**2 - ones, ones]
    
    while (m > 1):
        arr_next = [[-9999999] * (m//2) for _ in range(m//2)]
        for i in range(m//2):
            for j in range(m//2):
                s = 0
                for k in range(2):
                    for l in range(2):
                        s += arr[2*i + k][2*j + l]
                if s == 0:
                    arr_next[i][j] = 0
                    answer[0] -= 3
                if s == 4:
                    arr_next[i][j] = 1
                    answer[1] -= 3
        arr = arr_next
        m //= 2
    return answer