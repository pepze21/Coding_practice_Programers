cdd_keys = set()

def str_sum(list_str):
    s = ''
    for item in list_str:
        s += str(item)
    return s

def is_uniq(table):
    row_distinct = set()
    for row in table:
        row_distinct.add(','.join(row))
    return len(table) == len(row_distinct)

def dfs(keys, relation, l):
    if len(keys) == 1:
        cdd_keys.add(str_sum(keys))
        return
    
    cnt = 0
    for key in keys:
        sub_keys = keys.copy()
        sub_keys.remove(key)
        sub_rel = [[relation[i][k] for k in sub_keys] for i in range(l)]
        if is_uniq(sub_rel):
            cnt += 1
            dfs(sub_keys, relation, l)  
    if cnt == 0:
        cdd_keys.add(str_sum(keys)) # already sorted, thus not duplicated

def solution(relation):
    l = len(relation)
    keys = [i for i in range(len(relation[0]))]
    dfs(keys, relation, l)
    return len(cdd_keys)