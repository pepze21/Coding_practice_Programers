def solution(n, left, right):
    i1, j1 = divmod(left, n)
    i2, j2 = divmod(right, n)

    answer = []
    while (True):
        answer.append(max(i1 + 1, j1 + 1))
        if ((i1 == i2) and (j1 == j2)):
            break
        j1 = (j1 + 1) % n
        if j1 == 0:
            i1 = (i1 + 1) % n
            
    return answer

# 1분 짠 코드 : (당연히?) 시간초과
# def solution(n, left, right):
#     matrix = [[max(i + 1, j + 1) for i in range(n)] for j in range(n)]
#     arr = []
#     for row in matrix:
#         arr += row
#     return arr[left:right+1]