def solution(n,a,b):
    cnt = 0
    k = len(bin(n - 1)[2:])
    s1 = bin(a - 1)[2:].zfill(k)
    s2 = bin(b - 1)[2:].zfill(k)
    for i in range(k):
        if s1[i] == s2[i]:
            cnt += 1
        else:
            break
    return k - cnt