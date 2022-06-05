# move k from a to b
def move(a, b, k):
    if (k == 1):
        return [[a, b]]
    return move(a, 6 - a - b, k - 1) + [[a, b]] + move(6 - a - b, b, k - 1)

def solution(n):
    return move(1, 3, n)