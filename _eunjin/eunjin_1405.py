import sys
sys.setrecursionlimit(10**6)

N, e, w, s, n = map(int, input().split())

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

percent = [s, e, n, w]

visited = [[0]*(2*N+1) for _ in range(2*N+1)]

answer = 0


def dfs(y, x, p, cnt):
    global answer

    if cnt == N:
        answer += p
        return

    visited[y][x] = 1

    for i in range(4):
        ny = y+dy[i]
        nx = x+dx[i]
        if 0 <= ny < (2*N+1) and 0 <= nx < (2*N+1):
            if visited[ny][nx]:  # 이미 방문한 경우
                continue
            else:
                dfs(ny, nx, p*(percent[i]/100), cnt+1)  # 다음 자리 방문
                visited[ny][nx] = 0


dfs(N, N, 1, 0)

print(answer)
