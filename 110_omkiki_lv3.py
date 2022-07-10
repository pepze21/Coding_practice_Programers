def solution(s):
    answer = []
    for x in s:
        stack = []
        cnt_one = 0
        cnt_del = 0
        for c in x:
            if c == '0':
                if cnt_one < 2:
                    stack.append('0')
                    cnt_one = 0
                else:
                    stack.pop()
                    stack.pop()
                    cnt_one -= 2
                    cnt_del += 1
            elif c == '1':
                stack.append('1')
                cnt_one += 1
        x = ''.join(stack)

        if '11' in x:
            i = x.index('11')
        else:
            i = len(x)

        if (i - 1 >= 0) and (x[i - 1] == '1'):
            i -= 1
            
        # print(x, x[:i], '110' * cnt_del, x[i:], x[:i] + '110' * cnt_del + x[i:])
        answer.append(x[:i] + '110' * cnt_del + x[i:])
    return answer

# 더 빠른데 시간초과 뜸...?
# def solution(s):
#     answer = []
#     for x in s:
#         y = x
#         while (True):
#             tmp = len(y)
#             y = y.replace('110', '')
#             # print(x, y)
#             if tmp == len(y):
#                 break
#         if '11' in y:
#             index = y.index('11')
#         else:
#             index = len(y)

#         if (index - 1 >= 0) and (y[index - 1] == '1'):
#             index -= 1

#         answer.append(y[:index] + '110' * ((len(x) - len(y)) // 3) + y[index:])
#     return answer
        

# 틀림 : 정확한 이유는 모르겠으나 두번째 try except 문에서 문제발생
# def solution(s):
#     answer = []
#     for x in s:
#         y = x
#         while (True):
#             tmp = len(y)
#             y = y.replace('110', '')
#             if tmp == len(y):
#                 break
#         try:
#             index = y.index('11')
#         except:
#             index = len(y)
#         try:
#             if (y[index - 1] == '1'):
#                 index -= 1
#         except:
#             pass
#         answer.append(y[:index] + '110' * ((len(x) - len(y)) // 3) + y[index:])
#     return answer
        

# 틀림
# replace('110', '') 110이 없을때까지
# -> 적당한 위치에 '110' 추가
# def solution(s):
#     answer = []
#     for x in s:
#         y = x
#         print('before :', y)
#         while (True):
#             tmp = len(y)
#             y = y.replace('110', '')
#             if tmp == len(y):
#                 break
#         print('after :', y)
#         try:
#             index = y.index('11')
#         except:
#             index = len(y)
#         print("insert '110's at this index :", index)
#         if (y == '0'):
#             answer.append('0' + '110' * ((len(x) - len(y)) // 3))
#         elif (y == '1'):
#             answer.append('110' * ((len(x) - len(y)) // 3) + '1')
#         else:
#             answer.append(y[:index] + '110' * ((len(x) - len(y)) // 3) + y[index:])
#     print(answer)
#     return answer