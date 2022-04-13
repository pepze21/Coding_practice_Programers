def solution(answers):
    patterns = [
                [1, 2, 3, 4, 5],
                [2, 1, 2, 3, 2, 4, 2, 5],
                [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
               ]
    scores = [0] * 3
    
    for i in range(len(answers)):
        for j in range(3):
            if (patterns[j][i % len(patterns[j])] == answers[i]):
                scores[j] += 1

    answer = []
    for index, score in enumerate(scores):
        if (score == max(scores)):
            answer.append(index + 1)
    return answer