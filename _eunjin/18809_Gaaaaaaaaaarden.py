from itertools import combinations
from collections import deque
import sys
input = sys.stdin.readline

N, M, G, R = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

available = []  # 배양액 가능한 좌표
for y in range(N):
    for x in range(M):
        if matrix[y][x] == 2:
            available.append((y, x))

# 배양액 뿌릴 수 있는 모든 경우의 수에 대해 탐색해야함
total_comb = []  # 가능한 모든 초록색/빨간색 배양액 좌표 조합, total_comb[0][0]: 초록색 좌표 리스트, total_comb[0][1]: 빨간색 좌표 리스트
# [[(0, 3), (0, 5), (1, 6)], [(2, 0), (3, 2)]]

green_available = list(combinations(available, G))  # 배양액 가능한 초록색 좌표 조합

for green_comb in green_available:
    red_temp = []  # 배양액 가능한 빨간색 좌표 리스트
    for (y, x) in available:
        if (y, x) not in green_comb:
            red_temp.append((y, x))

    for red_comb in combinations(red_temp, R):  # 빨간색 배양액 뿌리는 좌표 조합
        total_temp = [[], []]
        for y, x in green_comb:
            total_temp[0].append((y, x))
        for y, x in red_comb:
            total_temp[1].append((y, x))
        total_comb.append(total_temp)  # 전체 좌표 조합 리스트에 해당 조합 추가

# bfs로 배양액 퍼트리기 + 꽃 피우기
def spread(comb):
    q = deque()
    visited = [[[-1, -1] for _ in range(M)] for _ in range(N)]  # visited[y][x][0]: (y,x) 좌표에 초록색이 뿌려진 시간
    flower = [[False] * M for _ in range(N)]
    flower_cnt = 0

    # 초록색 배양액 시작
    for y, x in comb[0]:
        q.append((y, x, 0, 0))  # y,x,color,time
        visited[y][x][0] = 0

    # 빨간색 배양액 시작
    for y, x in comb[1]:
        q.append((y, x, 1, 0))  # y,x,color,time
        visited[y][x][1] = 0

    while q:
        y, x, color, time = q.popleft()

        if flower[y][x]:  # 해당 좌표에 꽃 있으면 더이상 진행X
            continue

        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]

            if ny < 0 or ny >= N or nx < 0 or nx >= M:
                continue

            if matrix[ny][nx] == 0:  # 호수
                continue

            if flower[ny][nx]:  # 이미 꽃 피어있음
                continue

            if visited[ny][nx][color] != -1:  # 해당 좌표 해당 색상으로 이미 배양액 있음
                continue

            # 해당 좌표에 다른 색 배양액 있고 동시에 도달한 경우
            if visited[ny][nx][1 - color] != -1 and visited[ny][nx][1 - color] == time + 1:
                flower[ny][nx] = True
                flower_cnt += 1
                continue

            # 현재 색상 배양액 퍼트리기
            visited[ny][nx][color] = time + 1
            q.append((ny, nx, color, time + 1))

    return flower_cnt

answer = 0

for comb in total_comb:
    answer = max(answer, spread(comb))

print(answer)
