def solution(genres, plays):
    genres_set = set(genres)
    genres_sum = {} # {genre : # of play}
    for genre in genres_set:
        genres_sum[genre] = 0
    genres_two_songs = {} # {genre : [first_song, second_song]}
    
    for genre in genres_set:
        first_song = -1
        second_song = -1
        cnt = 0
        
        for i in range(len(genres)):
            if (genres[i] == genre):
                genres_sum[genre] += plays[i]
                cnt += 1
                if (cnt == 1):
                    first_song = i
                elif (cnt == 2):
                    if (plays[i] > plays[first_song]):
                        second_song = first_song
                        first_song = i
                    else:
                        second_song = i
                elif (plays[i] > plays[first_song]):
                    second_song = first_song
                    first_song = i
                elif (plays[i] > plays[second_song]):
                    second_song = i
                    
        genres_two_songs[genre] = [first_song]
        if (second_song != -1):
            genres_two_songs[genre] += [second_song]
    
    genres_sum_sorted = list(genres_sum.items())
    genres_sum_sorted = sorted(genres_sum_sorted, reverse=True, key=lambda x : x[1])
    
    answer = []    
    for i in range(len(genres_set)):
        answer += genres_two_songs[genres_sum_sorted[i][0]]
    
    return answer