def solution(arr):
    prime = [2, 3, 5, 7]
    for i in range(9, 101, 2):
        isprime = True
        for p in prime:
            if i % p == 0:
                isprime = False
                break
        if isprime:
            prime.append(i)
    
    answer = 1
    i = 0
    while (i < len(prime)):
        cnt = 0
        for j in range(len(arr)):
            if (arr[j] % prime[i] == 0):
                arr[j] //= prime[i]
                cnt += 1
        if cnt:
            answer *= prime[i]
        else:
            i += 1
            
    return answer    