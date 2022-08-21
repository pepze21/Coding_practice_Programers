def solution(arrows):
    answer = 0
    visit_v = set()
    visit_e = set()
    d = [[-1, +0],
         [-1, +1],
         [+0, +1],
         [+1, +1],
         [+1, +0],
         [+1, -1],
         [+0, -1],
         [-1, -1]]
    i = j = 0
    visit_v.add((i, j))
    cnt = 0
    for arrow in arrows:
        di, dj = d[arrow]
        cnt += 1
        pre_i = i
        pre_j = j
        i += di
        j += dj
        if ((i, j, pre_i, pre_j) not in visit_e) and ((i, j) in visit_v):
            answer += 1
        if ((i, j, pre_i, pre_j) not in visit_e) and (arrow % 2 != 0) and ((i, pre_j, pre_i, j) in visit_e):
            answer += 1
        visit_v.add((i, j))
        visit_e.add((i, j, pre_i, pre_j))
        visit_e.add((pre_i, pre_j, i, j))
    return answer