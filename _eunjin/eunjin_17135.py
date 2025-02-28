from itertools import combinations
from collections import deque
import copy

N, M, D = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(N)]

dy = [0, -1, 0]  # 왼, 위, 오
dx = [-1, 0, 1]

# 해당 열의 궁수의 공격 대상 좌표 탐색


def bfs(col):  # 해당 열의 제일 아래 칸부터 bfs 시작
    visited = [[False]*M for _ in range(N)]

    q = deque()
    q.append((N-1, col, 1))  # y,x,d
    visited[N-1][col] = True

    while q:
        y, x, d = q.popleft()

        if d > D:
            break

        if mat[y][x] == 1:
            return (y, x)

        for i in range(3):
            ny = y+dy[i]
            nx = x+dx[i]
            if 0 <= ny < N and 0 <= nx < M:
                if not visited[ny][nx]:
                    q.append((ny, nx, d+1))
                    visited[ny][nx] = True
    return False


# 궁수의 위치 조합
mx_cnt = 0
for archers in combinations(range(0, M), 3):
    mat = copy.deepcopy(matrix)
    cnt = 0

    for _ in range(N):  # 적들을 아래로 N-1번 이동
        attack = set()
        for arch in archers:  # 궁수 조합의 각 궁수에 대해
            node = bfs(arch)  # 공격 대상 탐색
            if node:  # 공격 가능한 적이 있으면
                attack.add(node)  # 공격 대상 set에 노드 추가

        cnt += len(attack)
        for y, x in attack:
            mat[y][x] = 0

        mat = [[0]*M] + mat[:N-1]  # 적 아래로 한칸씩 이동
    mx_cnt = max(cnt, mx_cnt)
    # print("archers:", archers, ", cnt:", cnt)

print(mx_cnt)
