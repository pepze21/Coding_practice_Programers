def solution(skill, skill_trees):
    answer = 0
    for skill_tree in skill_trees:
        i = -1
        for a in skill:
            if a in skill_tree:
                if (i < skill_tree.index(a)):
                    i = skill_tree.index(a)
                else:
                    break
            else:
                i = 99
            if (a == skill[-1]):
                answer += 1
    return answer