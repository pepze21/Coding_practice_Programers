def f(n):
    b = bin(n)[2:].zfill(17)
    for i in range(len(b)):
        if (b[len(b) - 1 - i] == '0'):
            break
    if i == 0:
        return n + 2**i
    else:
        return n + 2**i - 2**(i - 1)
    
def solution(numbers):
    answer = []
    for n in numbers:
        answer.append(f(n))
    return answer