def decomposition(w):
    count = 0
    if w[0] == '(':
        right = True # is u right?
    else:
        right = False
        
    for i in range(len(w)):
        if w[i] == '(':
            count += 1
        else:
            count -= 1
        if count == 0:
                return w[:i + 1], w[i + 1:], right

def recursion(w):
    if w == '':
        return ''
    
    u, v, right = decomposition(w)
    if right:
        return u + recursion(v)
    else:
        s = ''
        for c in u[1:-1]:
            if c == '(':
                s += ')'
            else:
                s += '('
        return '(' + recursion(v) + ')' + s
    
def solution(p):
    return recursion(p)