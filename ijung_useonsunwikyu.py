from collections import deque

def insertByBS(q, num):
    if (not q or q[-1] > num):
        return q.append(num)
    
    upper = len(q) - 1
    lower = 0
    mid = (upper + lower) // 2
    
    while(True):    
        if (num >= q[mid]):
            upper = mid
        elif (q[mid] > num):
            lower = mid + 1
        mid = (upper + lower) // 2
        if (upper == lower):
            return q.insert(mid, num)
    
def solution(operations):
    q = deque()

    for operation in operations:
        if (operation.split()[0] == 'I'):
            insertByBS(q, int(operation.split()[1]))
        else:
            if (operation.split()[1] == '1'):
                if (q):
                    q.popleft()
            else:
                if (q):
                    q.pop()
    
    answer = [0, 0]
    if (q):
        answer[0] = q.popleft()
        answer[1] = answer[0]
    if (q):
        answer[1] = q.pop()
    return answer