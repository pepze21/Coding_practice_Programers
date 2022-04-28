def solution(price, money, count):
    value = ((price * (count * (count + 1))) // 2) - money
    if value > 0:
        return value
    else:
        return 0 