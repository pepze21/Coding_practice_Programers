def solution(N, stages):

    u = {} # users_at_the_stage
    for i in range(N + 2):
        u[i] = 0
    for stage in stages:
        u[stage] += 1
    
    pfs_u = u.copy() # prefix of users_at_the_stage
    for i in range(N):
        pfs_u[N - i] += pfs_u[N + 1 - i]
    
    fail_rate = [(i, 0 if pfs_u[i] == 0 else u[i]/pfs_u[i]) for i in range(1, N + 1)]
    fail_rate = sorted(fail_rate, key=lambda x: -x[1])
    
    return [x[0] for x in fail_rate]