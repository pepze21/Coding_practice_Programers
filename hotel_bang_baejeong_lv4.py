from collections import defaultdict

def solution(k, room_number):
    pntr = defaultdict(list)
    answer = []
    for p in room_number:
        # p -> [] i.e. 빈 방
        if not pntr[p]:
            answer.append(p)
            if pntr[p + 1]:
                pntr[p] = pntr[p + 1]
            else:
                pntr[p].append(p + 1)
        else:
            # p, q, r : int
            r = q = p
            while (pntr[r]):
                pntr[q] = pntr[r]
                q = r
                r = pntr[r][0]
            answer.append(r)
            pntr[r] = pntr[q]
            pntr[q][0] += 1
    return answer