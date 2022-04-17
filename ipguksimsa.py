def solution(n, times):
    upper = min(times) * n
    lower = 0
    while (upper != lower):
        middle = (upper + lower) // 2
        num_of_finished_people = 0
        for time in times:
            num_of_finished_people += middle // time
        if (num_of_finished_people >= n):
            upper = middle
        else:
            lower = middle + 1
    return lower