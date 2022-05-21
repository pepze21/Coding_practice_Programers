def solution(number, k):
    end_condition = len(number) - k
    answer = ''
    while (True):
        max_digit = '-1'
        max_index = -1
        for i in range(k + 1):
            if (number[i] > max_digit):
                max_digit = number[i]
                max_index = i
                if max_digit == '9':
                    break
        answer += max_digit
        number = number[max_index + 1:]
        k -= max_index
        if (len(answer) == end_condition):
            break
    return answer

# 테스트 케이스 10번 시간초과
# def solution(number, k):
#     end_condition = len(number) - k
#     answer = ''
#     while (True):
#         max_digit = '0'
#         max_index = 0
#         for i in range(k + 1):
#             if (number[i] > max_digit):
#                 max_digit = number[i]
#                 max_index = i
#         answer += max_digit
#         number = number[max_index + 1:]
#         k -= max_index
#         if (len(answer) == end_condition):
#             break
#     return answer