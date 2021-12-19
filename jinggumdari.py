# 02:20 ~
from copy import deepcopy
maxmin = 0

def delete_rock(diff, k):
    global maxmin
    temp = deepcopy(diff)
    minimum = min(temp)
    indices = []
    i = 0
    try:
        while True:
            indices.append(temp.index(minimum, i))
            i = temp.index(minimum, i) + 1
    except:
        pass
    
    if k < 1:
        maxmin = max(min(temp), maxmin)
        # [2, 9, 3, 3, 4, 4] start
        # [11, 3, 3, 4, 4] step1
        # [14, 3, 4, 4] / [11, 6, 4, 4] / [11, 6, 4, 4] / [11, 3, 7, 4] step2
        # maxmin = 4
        # print('maxmin =', maxmin, '/ diff =', diff)
        
    else:
        for index in indices:
            # left
            if index > 0:
                diff_next = temp[:index - 1] + \
                            [temp[index - 1] + temp[index]] + \
                            temp[index + 1:]
                delete_rock(diff_next, k - 1)
            # right
            if index < len(temp) - 1:
                diff_next = temp[:index] + \
                            [temp[index] + temp[index + 1]] + \
                            temp[index + 2:]
                delete_rock(diff_next, k - 1)

def solution(distance, rocks, n):
    global maxmin
    if len(rocks) == n:
        return distance
    
    rocks.sort()
    
    diff = []
    for i in range(len(rocks) + 1):
        temp = [0] + rocks + [distance]
        diff.append(temp[i+1] - temp[i])
    
    delete_rock(diff, n)
    
    return maxmin
    
