def solution(name):
    ALPHABETS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    indices = []
    ud = 0
    for i in range(len(name)):
        if name[i] != 'A':
            metric = ALPHABETS.index(name[i])
            ud += min(metric, len(ALPHABETS) - metric)
            indices.append(i)
    if 0 not in indices:
        indices.append(0)
    indices.sort()
            
    if len(indices) == 0:
        return 0
    if len(indices) == 1:
        return ud + min(indices[0], len(ALPHABETS) - indices[0])
    
    lr = []
    for i in range(len(indices)):
        l = (len(name) - indices[i]) % len(name)
        r = indices[i - 1]
        lr.append(min(2 * l + r, l + 2 * r))
        
    return ud + min(lr)