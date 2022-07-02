# 억지구현
def solution(dirs):
    visit = [[0] * 21 for _ in range(21)]
    delta = dict()
    delta['U'] = (0, +1)
    delta['D'] = (0, -1)
    delta['R'] = (+1, 0)
    delta['L'] = (-1, 0)
    x, y = 5, 5
    
    for d in dirs:
        dx, dy = delta[d]
        x_moved = False
        y_moved = False
        if 0 <= (x + dx) <= 10:
            x += dx
            if dx != 0:
                x_moved = True
        if 0 <= (y + dy) <= 10:
            y += dy
            if dy != 0:
                y_moved = True
        if x_moved:
            visit[2*x - dx][2*y] = 1
        if y_moved:
            visit[2*x][2*y - dy] = 1
            
    # for row in visit:
    #     print(row)
    # print(map(sum, visit))
    
    return sum(map(sum, visit))


    

# 틀림 : 문제를 잘못읽어서 '방문한 길'이 아닌, 방문한 '칸'을 구함
# def solution(dirs):
#     # origin : (5, 5)
#     visit = [[0] * 11 for _ in range(11)]
#     delta = dict()
#     delta['U'] = (0, +1)
#     delta['D'] = (0, -1)
#     delta['R'] = (+1, 0)
#     delta['L'] = (-1, 0)
#     x, y = 5, 5
#    
#     for d in dirs:
#         dx, dy = delta[d]
#         if 0 <= (x + dx) <= 10:
#             x += dx
#         if 0 <= (y + dy) <= 10:
#             y += dy
#         visit[-y][x] = 1
#       
#     return sum(map(sum, visit))