from collections import deque

def solution(people, limit):
    cnt = 0
    
    q = deque(sorted(people))
    
    boat = []
    
    while (q):
        if (not boat):
            boat.append(q.pop())
        else:
            if (boat[0] + q[0] <= limit):
                q.popleft()
                boat.pop()
                cnt += 1
            elif (boat[0] + q[0] > limit):
                boat.pop()
                cnt += 1
    if (boat):
        cnt += 1
    return cnt