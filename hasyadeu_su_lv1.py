def solution(x):
    summation = 0
    for s in str(x):
        summation += int(s)
    return not (x % summation)