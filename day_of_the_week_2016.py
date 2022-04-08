def solution(a, b):
    days_of_the_week = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    max_date = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    dates_since_20160101 = -1
    for i in range(a):
        dates_since_20160101 += max_date[i]
    dates_since_20160101 += b
    return days_of_the_week[dates_since_20160101 % 7]