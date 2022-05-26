from math import sqrt
def solution(brown, yellow):
    # yellow = j * i
    # brown = 2(j + 1) + 2(i + 1) = 2(j + i) + 4
    # j >= i
    # return [j + 2, i + 2]
    
    # j, i are the solutions of ax^2 - bx + c == 0 where a, b, c are bellow
    a = 1
    b = ((brown - 4) / 2)
    c = yellow

    return [(b + sqrt(b**2 - 4*a*c))/(2*a) + 2, (b - sqrt(b**2 - 4*a*c))/(2*a) + 2]