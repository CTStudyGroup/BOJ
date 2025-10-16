from itertools import combinations

N, M = map(int, input().split())
favors = [list(map(int, input().split())) for _ in range(N)]

answer = 0

for comb in combinations([i for i in range(M)], 3):
    score = 0
    for n in range(N):
        score += max(favors[n][comb[0]], favors[n][comb[1]], favors[n][comb[2]])

    answer = max(answer, score)

print(answer)

