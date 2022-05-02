def trans(char, n, is_upper):
    alpha_u = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alpha_l = 'abcdefghijklmnopqrstuvwxyz'
    if is_upper:
        return alpha_u[(alpha_u.index(char) + n) % 26]
    else:
        return alpha_l[(alpha_l.index(char) + n) % 26]
    
def solution(s, n):
    answer = ''
    for i, char in enumerate(s):
        if char == ' ':
            answer += char
        else:
            answer += trans(char, n, char.isupper())
    return answer