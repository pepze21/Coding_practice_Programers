from collections import deque

def solution(cacheSize, cities):
    if cacheSize == 0:
        return 5 * len(cities)
    
    q = deque()
    answer = 0
    for city in cities:
        city = city.lower()
        if len(q) < cacheSize:
            if city in q:
                answer += 1
                q.remove(city)
                q.append(city)
            else:
                answer += 5
                q.append(city)
        else:
            if city in q:
                answer += 1
                q.remove(city)
                q.append(city)
            else:
                answer += 5
                q.popleft()
                q.append(city)
                
    return answer