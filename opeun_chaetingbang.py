def solution(record):
    answer = []
    id_nick = {}
    
    for line in record:
        if line.split()[0] != 'Leave':
            id_nick[line.split()[1]] = line.split()[2]
    for line in record:
        if line.split()[0] == 'Enter':
            answer.append('{}님이 들어왔습니다.'.format(id_nick[line.split()[1]]))
        elif line.split()[0] == 'Leave':
            answer.append('{}님이 나갔습니다.'.format(id_nick[line.split()[1]]))
            
    return answer