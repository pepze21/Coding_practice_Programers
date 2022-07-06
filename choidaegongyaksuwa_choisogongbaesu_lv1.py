def gcd(a, b): # a = bq + r (b != 0, 0 <= r < b), gcd(a, b) == gcd(b, r)
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)
    
def solution(n, m):
    return [gcd(n, m) , (n * m) // gcd(n, m)]