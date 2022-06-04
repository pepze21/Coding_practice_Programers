def solution(s):
    l = len(s)
    while (l > 0):
        for i in range(len(s) + 1 - l):
            substr = s[i:i + l]
            isPal = True
            for j in range(len(substr)//2):
                if substr[j] != substr[l - 1 - j]:
                    isPal = False
                    break
            if isPal:
                return l
        l -= 1

# 시간초과
# def isPalindrome(s):
#     if s == ''.join(list(reversed(s))):
#         return len(s)
#     else:
#         return 0
#
# def solution(s):
#     l = len(s)
#     while (l > 0):
#         for i in range(len(s) + 1 - l):
#             if s[i:i + l] == ''.join(list(reversed(s[i:i + l]))):
#                 return l
#         l -= 1

# 시간초과
# def isPalindrome(s):
#     if s == ''.join(list(reversed(s))):
#         return len(s)
#     else:
#         return 0
#
# def solution(s):
#     l = len(s)
#     while (l > 0):
#         for i in range(len(s) + 1 - l):
#             if isPalindrome(s[i:i + l]):
#                 return l
#         l -= 1

# abcklcba -> counterexample (the answer is 1 but not 3)
# def solution(s):
#     substr = set()
#     s_rvs = ''.join(list(reversed(s)))
#     l = len(s)
#     while (l > 0):
#         for i in range(len(s) + 1 - l):
#             substr.add(s_rvs[i:i + l])
#         for i in range(len(s) + 1 - l):
#             if s[i:i + l] in substr:
#                 return l
#         substr.clear()
#         l -= 1