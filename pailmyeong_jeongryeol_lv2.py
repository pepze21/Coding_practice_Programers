def solution(files):
    indices = []
    for i, file in enumerate(files):
        head = ''
        for j in range(len(file)):
            
            if not file[j].isdigit():
                head += file[j]
            else:
                break
        head = head.lower()
        number = ''
        for k in range(j, len(file)):
            if file[k].isdigit():
                number += file[k]
            else:
                break
        number = number.zfill(5)
        tail = file[k:]
        indices.append((head, number, i))
    indices.sort()
    
    return [files[index[2]] for index in indices ]