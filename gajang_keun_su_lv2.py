# greedy
def solution(numbers):
    numbers = list(map(str,numbers))
    
    max_len = 0
    for number in numbers:
        if len(number) > max_len:
            max_len = len(number)
            
    numbers.sort(key=lambda x: x.ljust(max_len, x[0]), reverse=True)
    
    cnt = 1
    while (cnt > 0):
        cnt = 0
        for i in range(len(numbers) - 1):
            if numbers[i] + numbers[i + 1] < numbers[i + 1] + numbers[i]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                cnt += 1
                
    answer = ''.join(numbers)
    
    if int(answer) == 0:
        return '0'
    else:
        return str(int(''.join(numbers)))