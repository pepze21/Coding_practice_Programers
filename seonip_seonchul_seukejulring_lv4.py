# 끝나는 시간을 이진탐색으로 찾은 뒤 -> 인덱스 + 1 리턴

def solution(n, cores):
    u = ((n // len(cores)) + 1) * max(cores) # time upperbound
    l = 0                                    # time lowerbound
    while (u - l > 1):
        m = (u + l) // 2
        cnt = 0
        for core in cores:
            cnt += m // core + 1
        if cnt >= n:
            u = m
        else:
            l = m
            
    MAX = 0
    cnt = 0
    for core in cores:
        cnt += l // core + 1
    if cnt >= n:
        T = l
        MAX = cnt
    else:
        T = u
        for core in cores:
            MAX += T // core + 1
            
    task = []
    for i, core in enumerate(cores):
        task.append([(T//core) * core, i + 1])
    task.sort(key=lambda x: x[:1] + x[-1:])
    
    # drop residues
    for _ in range(MAX - n):
        a = task.pop()
    return task[-1][-1]

# 문제를 잘못 이해 : 가장 마지막에 완료되는 작업을 어떤 core에서 수행하는지 return함
# (정답은, '완료'가 아니라 '시작' 기준)
# def solution(n, cores):
#     u = ((n // len(cores)) + 1) * max(cores) # time upperbound
#     l = 0                                    # time lowerbound

#     while (u - l > 1):
#         m = (u + l) // 2
#         cnt = 0
#         for core in cores:
#             cnt += m // core + 1
#         if cnt >= n:
#             u = m
#         else:
#             l = m
#     MAX = 0
#     cnt = 0
#     for core in cores:
#         cnt += l // core + 1
#     if cnt >= n:
#         T = l
#         MAX = cnt
#     else:
#         T = u
#         for core in cores:
#             MAX += T // core + 1
#     print(u, m, l, cnt, T, MAX)
#     task = []
#     for i, core in enumerate(cores):
#         task.append([(T//core) * core, (T//core + 1) * core, i + 1])
#     print(task)
#     task.sort(key=lambda x: x[:1] + x[-1:])
#     print(task)
#     # drop residues
#     for _ in range(MAX - n):
#         a = task.pop()
#     print(task)
#     return max(task, key=lambda x: x[1:])[2]

# 문제 잘못이해 : 틀림
# from queue import PriorityQueue

# def solution(n, cores):
#     u = ((n // len(cores)) + 1) * max(cores) # time upperbound
#     l = 0                                    # time lowerbound

#     while (u - l > 1):
#         m = (u + l) // 2
#         cnt = 0
#         for core in cores:
#             cnt += m // core
#         if cnt >= n:
#             u = m
#         else:
#             l = m
            
#     MAX = 0
#     cnt = 0
#     for core in cores:
#         cnt += l // core
#     if cnt >= n:
#         T = l
#         MAX = cnt
#     else:
#         T = u
#         for core in cores:
#             MAX += T // core
    
#     pq = PriorityQueue() # order by asc
#     pqcnt = 0 # for test
#     for i, core in enumerate(cores):
#         if (T % core == 0):
#             pqcnt += 1
#             pq.put((core, -i)) # order by core asc, i desc
            
#     # drop residues
#     for _ in range(MAX - n):
#         a = pq.get()

#     # print(u, m, l, T, MAX, n, pqcnt)
#     return -pq.get()[1] + 1



# 틀림
# from queue import PriorityQueue

# def solution(n, cores):
    
#     u = ((n // len(cores)) + 1) * max(cores) # time upperbound
#     l = 0                                    # time lowerbound

#     while (u - l > 1):
#         m = (u + l) // 2
#         cnt = 0
#         for core in cores:
#             cnt += m // core
#         if cnt > n:
#             u = m
#         else:
#             l = m
            
#     MAX = 0
#     cnt = 0
#     for core in cores:
#         cnt += l // core
#     if cnt > n:
#         T = l
#         MAX = cnt
#     else:
#         T = u
#         for core in cores:
#             MAX += T // core
    
#     pq = PriorityQueue() # order by asc
#     for i, core in enumerate(cores):
#         if (T % core == 0):
#             pq.put((core, -i)) # order by core asc, i desc

#     for _ in range(MAX - n):
#         pq.get()
#     return -pq.get()[1] + 1

# 틀림 + 시간초과
# from collections import defaultdict

# def solution(n, cores):
#     q_cores = defaultdict(int)
    
#     cnt = n
#     while (cnt > 0):
#         for i in range(len(cores)):
#             if (q_cores[i] == 0):
#                 q_cores[i] = cores[i]
#                 cnt -= 1
#                 if cnt == 0:
#                     break
#             else:
#                 q_cores[i] -= 1
    
#     answer = 0
#     max_t = 0
#     for i in range(len(cores)):
#         if max_t < q_cores[i]:
#             max_t = q_cores[i]
#             answer = i + 1
#     return answer