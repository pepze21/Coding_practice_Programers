from math import floor

def solution(str1, str2):
    mset_str1 = set()
    mset_str2 = set()
    n_inter = 0
    n_union = 0
    ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
    
    str1 = str1.lower()
    str2 = str2.lower()
    
    print(str1)
    print(str2)
    
    for i in range(len(str1) - 1):
        if (str1[i] in ALPHABET) and (str1[i + 1] in ALPHABET):
            temp = str1[i:i + 2]
            while temp in mset_str1:
                temp = temp + '1'
            mset_str1.add(temp)
    for i in range(len(str2) - 1):
        if (str2[i] in ALPHABET) and (str2[i + 1] in ALPHABET):
            temp = str2[i:i + 2]
            while temp in mset_str2:
                temp = temp + '1'
            mset_str2.add(temp)
            
    u_num = len(mset_str1.union(mset_str2))
    
    if u_num == 0:
        return 1 * 65536
    
    i_num = len(mset_str1.intersection(mset_str2))
    
    return floor((i_num / u_num) * 65536)
    
    
    