def solution(elements):
    l = len(elements)
    sums = elements.copy()
    sums_set = set(sums)
    # 길이가 (i + 1)인 연속 부분 수열의 합들(sums)을 중복제거(sums_set)
    for i in range(1, l):
        for j in range(l):
            sums[j] += elements[(j + i) % l]
        sums_set.update(sums)
        
    return len(sums_set)