def to_sec(time):
    sec = 0
    for i in range(3):
        sec += int(time.split(':')[i]) * 60**(2-i)
    return sec

def to_time(sec):
    return str(sec//3600).zfill(2) + ":" + str((sec//60)%60).zfill(2) + ":" + str(sec%60).zfill(2)

def solution(play_time, adv_time, logs):
    play_sec = to_sec(play_time)
    adv_sec = to_sec(adv_time)
    w = [0 for _ in range(play_sec + 2)] # wight_at_the_time
    
    # prefix_sum
    for log in logs:
        w[to_sec(log.split('-')[0]) + 1] += 1
        w[to_sec(log.split('-')[1]) + 1] += -1
        
    for _ in range(2):
        for i in range(len(w) - 1):
            w[i + 1] += w[i]
            
    t = [w[i + adv_sec] - w[i] for i in range(play_sec - adv_sec + 1)]
    
    return to_time(t.index(max(t)))
