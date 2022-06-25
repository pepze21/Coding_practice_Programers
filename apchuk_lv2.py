def solution(msg):
    ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    d = dict()
    for i, c in enumerate(ALPHABET):
        d[c] = i + 1
    last_idx = 26
    
    answer = []
    while (msg):
        for i in range(len(msg)):
            if msg[:len(msg) - i] in d:
                answer.append(d[msg[:len(msg) - i]])
                if i != 0:
                    last_idx += 1
                    d[msg[:len(msg) - i + 1]] = last_idx
                msg = msg[len(msg) - i:]
                break
                
    return answer