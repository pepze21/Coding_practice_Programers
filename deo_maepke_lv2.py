# 빨라졌는데 왜빠른지 모름
import heapq
def solution(scoville, K):
    q = []
    for val in scoville:
        if val < K:
            q.append(val)
    heapq.heapify(q)
    size = len(q)
    while (q):
        idx = heapq.heappop(q)
        if idx >= K:
            return size - (len(q) + 1)
        elif q:
            heapq.heappush(q, idx + (heapq.heappop(q) * 2))
        else:
            if len(scoville) == size:
                return -1
            else:
                return size

# 시간초과
# from queue import PriorityQueue

# def solution(scoville, K):
#     scoville.sort()
#     q = PriorityQueue()
#     for val in scoville:
#         if val < K:
#             q.put(val)
#     size = q.qsize()
    
#     while (not q.empty()):
#         idx = q.get()
#         if idx >= K:
#             return size - (q.qsize() + 1)
#         elif not q.empty():
#             q.put(idx + (q.get() * 2))
#         else:
#             if len(scoville) == size:
#                 return -1
#             else:
#                 return size

# from queue import PriorityQueue
# import heapq
# def solution(scoville, K):
#     q = scoville.copy()

#     while (True):
#         heapq.heapify(q)
#         idx1 = heapq.heappop(q)
#         if idx1 >= K:
#             return len(scoville) - (len(q) + 1)
#         elif q:
#             heapq.heapify(q)
#             idx2 = heapq.heappop(q)
#             idx3 = idx1 + (idx2 * 2)
#             heapq.heappush(q, idx3)
#         else:
#             return -1

# from queue import PriorityQueue

# def solution(scoville, K):
#     scoville.reverse()
#     q = PriorityQueue()
#     for val in scoville:
#         q.put(val)
    
#     while (True):
#         idx1 = q.get()
#         if idx1 >= K:
#             return len(scoville) - (q.qsize() + 1)
#         elif q:
#             idx2 = q.get()
#             idx3 = idx1 + (idx2 * 2)
#             q.put(idx3)
#         else:
#             return -1

# from collections import deque

# class MinHeap():
#     def __init__(self):
#         self.queue = deque()
        
#     def insert(self, n):
#         pass
    
#     def pop(self):
#         pass
#     def min_heapify(self):
#         pass
    
    
# def solution(scoville, K):
#     min_heap = MinHeap()
#     count = 0
#     for i in scoville:
#         min_heap.insert(i)
#     while (len(min_heap.queue) >= 2) and (min_heap.queue[0] < K):
#         min_1 = min_heap.queue.pop()
#         min_2 = min_heap.queue.pop()
#         min_heap.insert(min_1 + 2*min_2)
#         count += 1
        
#     if min_heap.queue[0] < K:
#         return -1
#     else:
#         return count