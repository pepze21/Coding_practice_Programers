def solution(s):
    parsed_s_with_count = []
    element = ''
    digits = '0123456789'
    
    for i in range(len(s)):
        if s[i] in digits: # s[i] : 0~9 -> generate element
            element += s[i]
        else: # s[i] : not 0~9 -> append element (with count)
            if element:
                if parsed_s_with_count:
                    for j in range(len(parsed_s_with_count)):
                        if element == parsed_s_with_count[j][0]:
                            parsed_s_with_count[j][1] += 1
                            break
                        elif j == len(parsed_s_with_count) - 1:
                            parsed_s_with_count.append([element, 1])
                else:
                    parsed_s_with_count.append([element, 1])
                element = ''
    parsed_s_with_count = sorted(parsed_s_with_count, key=lambda x: x[1], reverse=True)

    answer = []
    for item in parsed_s_with_count:
        answer.append(int(item[0]))
    return answer

# def solution(s):
#     parsed_s_with_count = []
#     element = ''

#     for i in range(len(s)):
#         try: # s[i] : 0~9 -> generate element
#             int(s[i])
#             element += s[i]
#         except: # s[i] : not 0~9 -> append element (with count)
#             if element:
#                 if parsed_s_with_count:
#                     for j in range(len(parsed_s_with_count)):
#                         if element == parsed_s_with_count[j][0]:
#                             parsed_s_with_count[j][1] += 1
#                             break
#                         elif j == len(parsed_s_with_count) - 1:
#                             parsed_s_with_count.append([element, 1])
#                 else:
#                     parsed_s_with_count.append([element, 1])
#                 element = ''
#     parsed_s_with_count = sorted(parsed_s_with_count, key=lambda x: x[1], reverse=True)

#     answer = []
#     for item in parsed_s_with_count:
#         answer.append(int(item[0]))
#     return answer