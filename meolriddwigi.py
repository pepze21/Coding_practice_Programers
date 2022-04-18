def solution(n):
    if (n == 1):
        return 1
    elif (n == 2):
        return 2
    else:
        i = 3
        a = 1
        b = 2
        while (i <= n):
            tmp = b
            b += a
            a = tmp
            i += 1
    return b % 1234567