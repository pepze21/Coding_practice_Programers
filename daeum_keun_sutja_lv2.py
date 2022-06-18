def solution(n):
    s = '0' + str(bin(n))[2:]
    for i in range(len(s) - 1):
        if (s[- i - 1] == '1' and s[- i - 2] == '0'):
            break
    cnt = len(s[len(s)- i:].replace('0', ''))
    s = s[:- i - 2] + '10' + '0' * (i - cnt) + '1' * cnt
    s = '0b' + s.lstrip('0')
    return int(s, 2)