from collections import defaultdict

def calc(t, fees):
    return fees[1] + fees[3] * max(0, ((t - fees[0] + fees[2] - 1) // fees[2]))

def solution(fees, records):
    d = dict()
    c = defaultdict(int)
    inf = 10000
    for rec in records:
        t, n, _ = rec.split()
        t = int(t.split(':')[0]) * 60 + int(t.split(':')[1])
        n = int(n)
        if n not in d:
            d[n] = t
        else:
            c[n] += t - d[n]
            del d[n]
    for n in d:
        c[n] += 1439 - d[n]
    
    answer = []
    for n in sorted(c.keys()):
        answer.append(calc(c[n], fees))
        
    return answer