# 베스트앨범
def solution(genres, plays):
    music = {}
    N = len(genres)
    for i in range(N):
        if genres[i] in music:
            music[genres[i]].append((plays[i], i))
        else:
            music[genres[i]] = [(plays[i], i)]
    
    sorted_genres = sorted((music.keys()), key=lambda x: sum(y[0] for y in music[x]), reverse=True)
    answer = []
    for genre in sorted_genres:
        selected_music = sorted(music[genre], key=lambda x: x[0], reverse=True)
        answer.extend([x[1] for x in selected_music[:2]])
    return answer

print(solution(["classic", "pop", "classic", "classic"], [500, 600, 150, 800]))