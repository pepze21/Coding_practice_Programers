def solution(arr):
    tmp = -1
    answer= []
    for a in arr:
        if a != tmp:
            answer.append(a)
            tmp = a
    return answer