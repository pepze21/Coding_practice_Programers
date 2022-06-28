from queue import PriorityQueue

def solution(jobs):
    jobs = sorted(jobs, key=lambda x: x[0])
    pq = PriorityQueue()
    fin_time = 0
    sum_time = 0
    i = 0
    # pq는 비어있든 안 비어있든 True, pq.empty()는 비어있을 때만 True
    while ((i < len(jobs)) or (not pq.empty())):
        if ((pq.empty()) and (fin_time < jobs[i][0])):
            fin_time = jobs[i][0]
        while ((i < len(jobs)) and (jobs[i][0] <= fin_time)):
            pq.put((jobs[i][1], jobs[i])) # 이 tuple element는 jobs[i][1]을 기준으로 오름차순 정렬(최소 힙)
            i += 1
        if (not pq.empty()):
            next_job = pq.get()[1]
            fin_time += next_job[1]
            sum_time += (fin_time - next_job[0])
    return sum_time // len(jobs)