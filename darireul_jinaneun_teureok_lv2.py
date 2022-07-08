from collections import deque

def solution(bridge_length, weight, truck_weights):
    w = 0 # weight of trucks on bridge
    t = 0 # time
    b = deque([0] * bridge_length) # bridge
    
    truck_weights.reverse()
    while (truck_weights):
        if (w - b[0] + truck_weights[-1] <= weight):
            truck_in = truck_weights.pop()
            b.append(truck_in)
            truck_out = b.popleft()
            w += (truck_in - truck_out)
            t += 1
        else:
            b.append(0)
            w -= b.popleft()
            t += 1
            
    return t + bridge_length