from itertools import permutations

def operate(a, operand, b):
    if (operand == '+'):
        return a + b
    if (operand == '-'):
        return a - b
    if (operand == '*'):
        return a * b

def calculate(exp_list, priority):
    for operand in priority:
        while (operand in exp_list):
            index = exp_list.index(operand)
            exp_list[index - 1] = operate(exp_list[index - 1], exp_list[index], exp_list[index + 1])
            del exp_list[index]
            del exp_list[index]
    return exp_list[0]

def solution(expression):
    exp_list = []
    s = ''
    for i in range(len(expression)):
        if (expression[i].isdigit()):
            s += expression[i]
        else:
            exp_list.append(int(s))
            s = ''
            exp_list.append(expression[i])
    exp_list.append(int(s))
    
    scores = []
    for priority in permutations(['+', '-', '*'], 3):
        scores.append(calculate(exp_list.copy(), priority))
        
    return max(map(abs, scores))

# from itertools import permutations

# def operator(s, operand):
#     if s == '':
#         return ''
#     i = left = right = s.index(operand)
#     while (True):
#         if (left - 1 >= 0) and s[left - 1].isdigit():
#             left -= 1
#         else:
#             break
#     while (True):
#         if (right + 1 < len(s)) and s[right + 1].isdigit():
#             right += 1
#         else:
#             break
#     # print(left, i, right)
#     # print('xxxxxx', int(s[left:i]))
#     # print('xxxxxx',int(s[i + 1:right + 1]))
#     # print('xxxxxx', s[:left] + str(int(s[left:i]) + int(s[i + 1:right + 1])) + s[right + 1:])
#     # return ''
    
#     if operand == '+':
#         return s[:left] + str(int(s[left:i]) + int(s[i + 1:right + 1])) + s[right + 1:]
#     if operand == '-':
#         return s[:left] + str(int(s[left:i]) - int(s[i + 1:right + 1])) + s[right + 1:]
#     if operand == '*':
#         return s[:left] + str(int(s[left:i]) * int(s[i + 1:right + 1])) + s[right + 1:]

# def solution(expression):
#     operands = ['+', '-', '*']
#     for case in permutations(operands, 3):
#         answers = []
#         s = expression
#         print(case)
#         for operand in case:
#             print(operand)
#             while (operand in s):
#                 try:
#                     print('before:',s)
#                     s = operator(s, operand)
#                     print('after:',s)
#                 except:
#                     print(s)
#                     break

# # 연산 결과가 -가 나오는 경우, 문제가 발생함. 따라서 list에 split 해서 처리하는게 좋을듯
# from itertools import permutations

# def operator(s, operand):
#     if s == '':
#         return ''
#     i = left = right = s.index(operand)
#     while (True):
#         if (left - 1 >= 0) and s[left - 1].isdigit():
#             left -= 1
#         else:
#             break
#     while (True):
#         if (right + 1 < len(s)) and s[right + 1].isdigit():
#             right += 1
#         else:
#             break
#     # print(left, i, right)
#     # print('xxxxxx', int(s[left:i]))
#     # print('xxxxxx',int(s[i + 1:right + 1]))
#     # print('xxxxxx', s[:left] + str(int(s[left:i]) + int(s[i + 1:right + 1])) + s[right + 1:])
#     # return ''
    
#     if operand == '+':
#         return s[:left] + str(int(s[left:i]) + int(s[i + 1:right + 1])) + s[right + 1:]
#     if operand == '-':
#         return s[:left] + str(int(s[left:i]) - int(s[i + 1:right + 1])) + s[right + 1:]
#     if operand == '*':
#         return s[:left] + str(int(s[left:i]) * int(s[i + 1:right + 1])) + s[right + 1:]

# def solution(expression):
#     operands = ['+', '-', '*']
#     for case in permutations(operands, 3):
#         answers = []
#         s = expression
#         print(case)
#         for operand in case:
#             print(operand)
#             while (operand in s):
#                 try:
#                     print('before:',s)
#                     s = operator(s, operand)
#                     print('after:',s)
#                 except:
#                     print(s)
#                     break
                