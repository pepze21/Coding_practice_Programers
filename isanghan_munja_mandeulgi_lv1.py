def solution(s):
    answer = ''
    
    cnt = 0
    for i, char in enumerate(s):
        if char == ' ':
            cnt = 0
            answer += char
            continue
        
        if cnt % 2 == 0:
            cnt += 1
            answer += char.upper()
        else:
            cnt += 1
            answer += char.lower()
            
    return answer