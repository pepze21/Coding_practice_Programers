from copy import copy

def plus(a, b):
    return (a[0] + b[0], a[1] + b[1])
def minus(a, b):
    return (a[0] - b[0], a[1] + b[1])
def multiple(a, b):
    return (a[0] * b[0], a[1] + b[1])
def divide(a, b):
    return (a[0] // b[0], a[1] + b[1])


def solution(N, number):
    values = {(N*1, 1)}
    
    if N == number:
        return 1
    temp = copy(values)
    temp.add((N*11, 2))
    temp.add((N*111, 3))
    temp.add((N*1111, 4))
    temp.add((N*11111, 5))
    temp.add((N*111111, 6))
    temp.add((N*1111111, 7))
    temp.add((N*11111111, 8))
    minimum = 9
    
    for a in values:
        for b in values:
            temp.add(plus(a, b))
            temp.add(minus(a, b))
            temp.add(multiple(a, b))
            if b[0] != 0:
                temp.add(divide(a, b))
        for value in temp:
            if value[0] == number:
                if value[1] <=8:
                    minimum = min(value[1], minimum)
    if minimum < 3:
        return minimum

    values = copy(temp)
    for a in values:
        for b in values:
            temp.add(plus(a, b))
            temp.add(minus(a, b))
            temp.add(multiple(a, b))
            if b[0] != 0:
                temp.add(divide(a, b))
        for value in temp:
            if value[0] == number:
                if value[1] <=8:
                    minimum = min(value[1], minimum)
    if minimum < 4:
        return minimum
    
    values = copy(temp)
    for a in values:
        for b in values:
            temp.add(plus(a, b))
            temp.add(minus(a, b))
            temp.add(multiple(a, b))
            if b[0] != 0:
                temp.add(divide(a, b))
        for value in temp:
            if value[0] == number:
                if value[1] <=8:
                    minimum = min(value[1], minimum)
    if minimum <= 8:
        return minimum
    else:
        return -1