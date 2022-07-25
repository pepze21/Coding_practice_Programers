def solution(routes):
    answer = 0
    s_points = [] # start-point
    e_points = [] # end-point
    for index, route in enumerate(routes):
        s_points.append([route[0], index]) # start-point
        e_points.append([route[1], index]) # end-point
    s_points.sort(reverse=True)
    e_points.sort(reverse=True)
    
    while (s_points or e_points):
        indices = []
        index = s_points.pop()[1]
        for i in range(1, len(e_points) + 1):
            if (e_points[-i][1] == index):
                if (i == 1):
                    end = e_points.pop()[0]
                else:
                    del e_points[-i]
                    end, index = e_points.pop()
                    indices.append(index)
                break

        for _ in range(len(s_points)):
            if (s_points[-1][0] <= end):
                indices.append(s_points.pop()[1])
            else:
                break

        i = 1
        while (indices):
            index = indices.pop()
            for i in range(1, len(e_points) + 1):
                if (e_points[-i][1] == index):
                    del e_points[-i]
                    break
        
        answer += 1
    return answer