from itertools import permutations

def solution(k, dungeons):
    answer = 0
    for case in permutations(dungeons):
        cnt = 0
        l = k
        for dungeon in case:
            if l >= dungeon[0]:
                l -= dungeon[1]
                cnt += 1
            else:
                break
        if answer < cnt:
            answer = cnt
    return answer