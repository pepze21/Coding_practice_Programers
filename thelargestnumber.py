# the largest number

def solution(numbers):
    for i in range(len(numbers)):
        numbers[i] = str(numbers[i])
    numbers.sort()
    numbers.reverse()
    answer = ''.join(numbers)
    print(numbers)
    return answer