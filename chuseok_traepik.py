def solution(lines):
    points = [] # starting or ending points
    for line in lines:
        _, t, l= line.split()
        h, m, s = t.split(':')
        
        end_time = (int(h) * 3600000) + (int(m) * 60000) + int(s.replace('.', '')) # ending points
        start_time = end_time - int(l.replace('.', '').replace('s', '000')[:4]) + 1
        points.append([start_time - 999, 1]) # +1 when starting point of line in lines is in the interval(1s)
        points.append([end_time + 1, -1]) # -1 right after ending point
    
    points = sorted(points, key=lambda x: (x[0], x[1]))
    prefix_sum = [point[1] for point in points]
    # print(points)
    # print(prefix_sum)
    
    for i in range(len(prefix_sum) - 1):
        prefix_sum[i + 1] += prefix_sum[i]
    # print(prefix_sum)
    
    return max(prefix_sum)