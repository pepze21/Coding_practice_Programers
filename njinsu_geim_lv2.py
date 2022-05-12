def to_base_n(num, n):
    stack = []
    digit = '0123456789ABCDEF'
    a = num
    while (a > 0):
        a, b = divmod(a, n)
        stack.append(digit[b])
    return ''.join(reversed(stack))

def solution(n, t, m, p):
    s = '0'
    i = 0
    while (len(s) < m * t):
        s += to_base_n(i, n)
        i += 1
        
    answer = ''
    for i in range(p - 1, p - 1 + (m * t), m):
        answer += s[i]
    return answer