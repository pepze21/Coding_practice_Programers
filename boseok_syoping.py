from collections import deque

def solution(gems):
    gems_set = set(gems)
    kind_of_gems = len(gems_set)
    q = deque(gems)
    gems_count = {}
    start = 0
    end = 0
    history = []

    for gem in gems:
        if (gem in gems_count):
            gems_count[gem] += 1
        else:
            gems_count[gem] = 1
        q.append(gem)
        end += 1
        
        if (len(gems_count) == kind_of_gems):
            while (True):
                gem_pop = q.popleft()
                gems_count[gem_pop] -= 1
                start += 1
                if gems_count[gem_pop] == 0:
                    del gems_count[gem_pop]
                    history.append([start, end])
                    break
                  
    return sorted(history, key=(lambda x: x[1] - x[0]))[0]