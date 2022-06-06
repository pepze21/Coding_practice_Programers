def solution(s):
    answer = ''
    prev = ' '
    for i in range(len(s)):
        if prev == ' ':
            answer += s[i].upper()
        else:
            answer += s[i].lower()
        prev = s[i]
    return answer

# 틀림 split 하면 공백이 다 지워져서 안되는듯?
# def solution(s):
#     words = s.split()
#     for i, word in enumerate(words):
#         words[i] = word[0].upper() + word[1:].lower()
#     return ' '.join(words)