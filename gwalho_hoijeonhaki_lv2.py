def isright(s):
    tmp = len(s) + 1
    while (tmp > len(s)):
        tmp = len(s)
        s = s.replace('[]', '').replace('{}', '').replace('()', '')
    if s == '':
        return True
    else:
        return False

def solution(s):
    answer = 0
    for _ in range(len(s)):
        if isright(s):
            answer += 1
        s = s[1:] + s[0]
    return answer