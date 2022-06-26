def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        s = ''
        for _ in range(n):
            s = str((arr1[i] % 2) or (arr2[i] % 2)) + s
            arr1[i] //= 2
            arr2[i] //= 2
        answer.append(s.replace('1', '#').replace('0', ' '))
    return answer