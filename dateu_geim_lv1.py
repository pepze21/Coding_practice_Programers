def solution(dartResult):
    interval = [] # starting points of integer
    
    i = 0
    while (i < len(dartResult)):
        if dartResult[i].isdigit():
            interval.append(i)
            i += 2
        else:
            i += 1
    interval.append(i)
    
    scores = []
    for i in range(len(interval) - 1):
        tmp = dartResult[interval[i]:interval[i + 1]]
        
        if tmp[1].isdigit():
            a = 10
        else:
            a = int(tmp[0])
            
        if ('S' in tmp):
            b = 1 
        elif ('D' in tmp):
            b = 2
        elif ('T' in tmp):
            b = 3
            
        if ('*' in tmp):
            scores.append(2 * a**b)
            if (i >= 1):
                scores[-2] *= 2
        elif ('#' in tmp):
            scores.append((-1) * a**b)
        else:
            scores.append(a**b)
    return sum(scores)
            
