from collections import deque
def int_to_str(time):
    return str(time // 60).zfill(2) + ':' + str(time % 60).zfill(2)
def solution(n, t, m, timetable):
    q = deque(map(lambda x: int(x[:2]) * 60 + int(x[3:]), sorted(timetable)))
    flag = True
    tmp = 540 + ((n - 1) * t)
    for i in range(n):
        for _ in range(m):
            if (q) and (q[0] <= (540 + i * t)):
                flag = False
                tmp = q.popleft()
            else:
                flag = True
                tmp = 540 + ((n - 1) * t)
    if flag:
        return int_to_str(tmp)
    else:
        return int_to_str(tmp - 1)