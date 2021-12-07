def tri(num):
    str = ''
    
    while True:
        r = num % 3
        num = num // 3
        if r == 0:
            str = '1' + str
        elif r == 1:
            str = '2' + str
        else:
            str = '4' + str
        if num == 0:
            return str

def solution(n):
    l = 1 # length
    temp = n
    
    while True:
        temp -= 3**l
        if temp > 0:
            l += 1
        else:
            temp += 3**l
            break
    
    answer = tri(temp - 1)

    if l != len(answer):
        for i in range(l - len(answer)):
            answer = '1' + answer
    
    return answer