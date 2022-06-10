def solution(phone_book):
    p_set = set(phone_book)
    for p_num in phone_book:
        for i in range(1, len(p_num)):
            if p_num[:i] in p_set:
                return False
    return True

# hash set 안씀 -> 시간초과
# def solution(phone_book):            
#     phone_book.sort(key=len)
    
#     for i, p_num in enumerate(phone_book):
#         for j in range(i + 1, len(phone_book)):
#             if (p_num == phone_book[j][:len(p_num)]):
#                 return False
            
#     return True