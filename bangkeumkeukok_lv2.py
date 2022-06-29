def time_to_min(time):
    h, m = time.split(':')
    return int(h) * 60 + int(m)

def solution(m, musicinfos):
    answers = []
    for seq, musicinfo in enumerate(musicinfos):
        start, end, title, notes = musicinfo.split(',')
        notes_list = []
        i = len(notes) - 1
        while (i >= 0):
            if notes[i] == '#':
                notes_list.append(notes[i - 1] + notes[i])
                i -= 2
            else:
                notes_list.append(notes[i])
                i -= 1
        notes_list.reverse()
        notes_played = []
        t = time_to_min(end) - time_to_min(start)
        for i in range(t):
            notes_played.append(notes_list[i % (len(notes_list))])
            if (len(m) <= len(''.join(notes_played))) and (m == ''.join(notes_played[-(len(m) - m.count('#')):])):
                answers.append((t, -seq, title))
                break
                
    if answers:
        return max(answers)[2]
    else:
        return '(None)'