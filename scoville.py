
from collections import deque

class MinHeap():
    def __init__(self):
        self.queue = deque()
        
    def insert(self, n):
        pass
    
    def pop(self):
        pass
    def min_heapify(self):
        pass
    
    
def solution(scoville, K):
    min_heap = MinHeap()
    count = 0
    for i in scoville:
        min_heap.insert(i)
    while (len(min_heap.queue) >= 2) and (min_heap.queue[0] < K):
        min_1 = min_heap.queue.pop()
        min_2 = min_heap.queue.pop()
        min_heap.insert(min_1 + 2*min_2)
        count += 1
        
    if min_heap.queue[0] < K:
        return -1
    else:
        return count