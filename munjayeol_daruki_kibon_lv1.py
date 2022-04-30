def solution(s):
    if len(s) not in (4, 6):
        return False
    for char in s:
        if not char.isdigit():
            return False
    return True