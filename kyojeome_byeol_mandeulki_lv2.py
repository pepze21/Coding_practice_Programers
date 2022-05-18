def solution(line):
    pnts = set()
    for i in range(len(line) - 1):
        for j in range(i + 1, len(line)):
            A, B, E = line[i]
            C, D, F = line[j]
            n1 = B * F - E * D
            n2 = E * C - A * F
            dn = A * D - B * C
            if dn != 0 and n1 % dn == 0 and n2 % dn == 0:
                pnts.add((n1 // dn, n2 // dn))
                
    inf = 20000000001
    min_x = +inf
    max_x = -inf
    min_y = +inf
    max_y = -inf
    for pnt in pnts:
        if max_x < pnt[0]:
            max_x = pnt[0]
        if min_x > pnt[0]:
            min_x = pnt[0]
        if max_y < pnt[1]:
            max_y = pnt[1]
        if min_y > pnt[1]:
            min_y = pnt[1]
    
    grid = [['.'] * (max_x - min_x + 1) for _ in range(max_y - min_y + 1)]
    for pnt in pnts:
        grid[max_y - pnt[1]][pnt[0] - min_x] = '*'
        
    return list(map(''.join, grid))