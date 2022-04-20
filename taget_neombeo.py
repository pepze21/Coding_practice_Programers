CNT = 0
SUM = 0

def n_times_for(n, numbers, target):
    global CNT, SUM
    for sign in [1, -1]:
        SUM += sign * numbers[n-1]
        if n - 1 > 0:
            n_times_for(n - 1, numbers, target)
        else:
            if SUM == target:
                CNT += 1
        SUM -= sign * numbers[n - 1]
    
def solution(numbers, target):
    global CNT, SUM
    n_times_for(len(numbers), numbers, target)
    return CNT