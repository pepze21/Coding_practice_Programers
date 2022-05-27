def dp(k, cnt, pnt, tf, tmp, answers, n, info):
    if k == 10:
        answers.append((pnt, tmp.copy()))
        return
    
    if tf == 0:
        tmp.append(0)
        dp(k + 1, cnt, pnt, 0, tmp, answers, n, info)
        tmp.pop()
        tmp.append(0)
        dp(k + 1, cnt, pnt, 1, tmp, answers, n, info)
        tmp.pop()
    else:
        if cnt + info[k] + 1 <= n:
            if info[k] == 0:
                tmp.append(info[k] + 1)
                dp(k + 1, cnt + (info[k] + 1), pnt + (10 - k), 0, tmp, answers, n, info)
                tmp.pop()
                tmp.append(info[k] + 1)
                dp(k + 1, cnt + (info[k] + 1), pnt + (10 - k), 1, tmp, answers, n, info)
                tmp.pop()
            else:
                tmp.append(info[k] + 1)
                dp(k + 1, cnt + (info[k] + 1), pnt + 2 * (10 - k), 0, tmp, answers, n, info)
                tmp.pop()
                tmp.append(info[k] + 1)
                dp(k + 1, cnt + (info[k] + 1), pnt + 2 * (10 - k), 1, tmp, answers, n, info)
                tmp.pop()
        else:
            tmp.append(0)
            dp(k + 1, cnt, pnt, 0, tmp, answers, n, info)
            tmp.pop()
            tmp.append(0)
            dp(k + 1, cnt, pnt, 1, tmp, answers, n, info)
            tmp.pop()
            answers.append((pnt, tmp.copy()))
            
def solution(n, info):
    score = 0
    for i, cnt in enumerate(info):
        if cnt > 0:
            score += (10 - i)
    
    answers = []
    dp(0, 0, 0, 0, [], answers, n, info)
    dp(0, 0, 0, 1, [], answers, n, info)
    
    for i in range(len(answers) - 1, -1, -1):
        if ((answers[i][1]) and (answers[i][1][-1] == 0)):
            del answers[i]
            
    highest = max(answers, key= lambda x: (x[0], len(x[1]), x[-1]))
    if (highest[0] <= score):
        return [-1]
    
    answer = highest[1]
    
    while (len(answer) < 10):
        answer.append(0)
    if len(answer) == 10:
        answer.append(n - sum(answer))
        
    return answer    