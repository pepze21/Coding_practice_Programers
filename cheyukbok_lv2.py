def solution(n, lost, reserve):
    lost_copy = lost.copy()
    for i in lost_copy:
        if i in reserve:
            lost.remove(i)
            reserve.remove(i)
    answer = n - len(lost)
    lost.sort()
    reserve.sort()
    for i in lost:
        if (i - 1) in reserve:
            reserve.remove(i - 1)
            answer += 1
        elif (i + 1) in reserve:
            reserve.remove(i + 1)
            answer += 1
    return answer