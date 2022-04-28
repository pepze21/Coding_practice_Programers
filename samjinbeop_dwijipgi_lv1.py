def solution(n):
    stack = []
    
    while (n > 0):
        stack.append(n % 3)
        n //= 3

    answer = 0
    for i in range(len(stack)):
        answer += (stack.pop() * (3**i))
    return answer