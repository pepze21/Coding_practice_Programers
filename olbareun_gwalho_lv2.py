def solution(s):
    a = 0
    for char in s:
        if char == '(':
            a += 1
        else:
            a -= 1
        if a < 0:
            return False
    if a != 0:
        return False
    else:
        return True