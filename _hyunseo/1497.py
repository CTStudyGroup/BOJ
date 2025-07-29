from itertools import combinations

N, M = map(int, input().split())
guitars = []

for _ in range(N):
    name, songs = input().split()
    playable = {i for i, ch in enumerate(songs) if ch == 'Y'}
    guitars.append(playable)

max_song = 0       # 연주 가능한 최대 곡 수
min_guitar = 11    # 최소 기타 개수

# 1개 이상 모든 조합 탐색
for r in range(1, N+1):
    for comb in combinations(guitars, r):
        combined = set()
        for g in comb:
            combined |= g   # 합집합 **** 중요! 
        song_cnt = len(combined)  # 연주 가능 곡 수

        if song_cnt > max_song:
            max_song = song_cnt
            min_guitar = r
        elif song_cnt == max_song:
            min_guitar = min(min_guitar, r)

# 연주할 수 있는 곡이 하나도 없으면 -1
print(-1 if max_song == 0 else min_guitar)
