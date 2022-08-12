def solution(money):
    # case 0 : 최초로 턴 집이 0번째 집인 경우
    # a0[i] == 0 ~ i번째 집에서 훔칠 수 있는 돈의 최댓값
    if (len(money) == 3):
        return max(money)
    a0 = money[:-1]
    a0[0] = money[0]
    a0[1] = 0
    a0[2] = money[0] + money[2]
    if ((len(money) - 1) > 3):
        for i in range(3, len(money) - 1):
            a0[i] += max(a0[i - 3], a0[i - 2])

    # case 1 : 최초로 턴 집이 1번째 집인 경우
    # a1[i] == 0 ~ i번째 집에서 훔칠 수 있는 돈의 최댓값
    a1 = money[:]
    a1[0] = 0
    a1[1] = money[1]
    a1[2] = 0
    if (len(money) > 3):
        for i in range(3, len(money)):
            a1[i] += max(a1[i - 3], a1[i - 2])
    
    # case 2 : 최초로 턴 집이 2번째 집인 경우
    # a2[i] == 0 ~ i번째 집에서 훔칠 수 있는 돈의 최댓값
    # 이 경우 money[-1]을 훔치는 경우만 최댓값 후보에 넣으면 됨 (a2[-1:])
    # (case2에서 money[-1]을 훔치지 않는 경우는 최댓값이 될 수 없음.
    # 왜냐하면 그 때 추가로 money[1]를 훔치는 경우(case 1) 더 커지기 때문)
    a2 = money[:]
    a2[0] = 0
    a2[1] = 0
    a2[2] = money[2]
    a2[3] = 0
    if (len(money) > 4):
        for i in range(4, len(money)):
            a2[i] += max(a2[i - 3], a2[i - 2])

    # 빼먹은 케이스
    a3 = money[:-1]
    a3[0] = money[0]
    a3[1] = 0
    a3[2] = 0
    if ((len(money) - 1) > 3):
        for i in range(3, len(money) - 1):
            a3[i] += max(a3[i - 3], a3[i - 2])
    
    return max(a0[-2:] + a1[-2:] + a2[-1:] + a3[-2:])
