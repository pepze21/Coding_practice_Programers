from collections import deque

def solution(priorities, location):
    p = []
    for loc, priority in enumerate(priorities):
        p.append((priority, loc))
    q = deque(p)
    priorities.sort()
    
    cnt = 0
    while (q):
        q_pop = q.popleft()
        if q_pop[0] < priorities[-1]:
            q.append(q_pop)
        else:
            cnt += 1
            priorities.pop()
            if q_pop[1] == location:
                return cnt