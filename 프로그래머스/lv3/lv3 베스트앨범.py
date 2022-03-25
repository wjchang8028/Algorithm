def solution(genres, plays):
    answer = []
    hash_playlist = {}

    for i in range(len(genres)):
        if genres[i] in hash_playlist:
            hash_playlist[genres[i]].append([plays[i],i])
        else:
            hash_playlist[genres[i]] = [[plays[i],i]]
    print(hash_playlist)

    genres_rank = {}

    for genre in hash_playlist.keys():
        songs = hash_playlist[genre]
        
        plays_sum = 0
        for song in songs:
            plays_sum += song[0]
        genres_rank[genre] = plays_sum
    
    genres_rank = sorted(genres_rank.items(), key= lambda x: x[1],reverse=True)
    print(genres_rank)
    
    for genre in genres_rank:
        song_rank = sorted(hash_playlist[genre[0]], key= lambda x:(-x[0],x[1])) # 재생수 기준 내림차순 , 고유번호 오름차순
        
        count_two = 0
        for song in song_rank:
            answer.append(song[1])
            count_two += 1
            if count_two == 2:
                break
    
    print(answer)
    return answer

solution(["classic", "pop", "classic", "classic", "pop"],[500, 600, 150, 800, 2500])