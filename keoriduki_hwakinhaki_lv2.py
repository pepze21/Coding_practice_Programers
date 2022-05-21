def metric(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def isRight(place):
    people = []
    for i in range(5):
        for j in range(5):
            if place[i][j] == 'P':
                people.append((i, j))
    for i in range(len(people)):
        for j in range(i + 1, len(people)):
            if metric(people[i], people[j]) == 1:
                return 0
            elif metric(people[i], people[j]) == 2:
                if people[i][0] == people[j][0] or people[i][1] == people[j][1]:
                    if place[(people[i][0] + people[j][0]) // 2][(people[i][1] + people[j][1]) // 2] != 'X':
                        return 0
                else:
                    if place[people[i][0]][people[j][1]] != 'X' or place[people[j][0]][people[i][1]] != 'X':
                        return 0
    return 1
                        
def solution(places):
    answer = []
    for place in places:
        answer.append(isRight(place))
    return answer  