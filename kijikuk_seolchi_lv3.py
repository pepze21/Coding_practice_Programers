# return (min) + (additional construction by unnecessary distance loss) + (previously constructed)
def solution(n, stations, w):
    s = 2 * w + 1 # size
    mdl = (s - n % s) % s # minimal distance loss
    stations = [-w] + stations + [n + w + 1]
    
    for i in range(len(stations) - 1):
        stations[i] = (s - (stations[i + 1] - stations[i]) % s) % s
        
    return ((n - 1) // s + 1) + ((sum(stations[:-1]) - mdl - 1) // s + 1) - (len(stations) - 2)