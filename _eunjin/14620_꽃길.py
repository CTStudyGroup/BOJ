import sys
input = sys.stdin.readline

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

# N<=10이므로 N*N 좌표에 대해 3개 고르는 완전탐색 가능
# 백트래킹으로 하나 고르고 -> 다음 진행 -> 고른거 취소 하자

def get_total_price():
    ret = 0
    for y, x in arr:
        ret += matrix[y][x]
        for i in range(4):
            ret += matrix[y + dy[i]][x + dx[i]]

    return ret

def can_visit(y, x):
    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if ny < 0 or ny >= N or nx < 0 or nx >= N:
            return False
        if visited[ny][nx]:
            return False
    return True


def backtracking(y, x):
    global answer
    if len(arr) == 3:
        answer = min(answer, get_total_price())
        return

    for ny in range(N):
        for nx in range(N):
            if ny == y and nx == x:
                continue
            if can_visit(ny, nx) and (ny, nx) not in arr:
                # 방문 처리
                arr.append((ny, nx))
                visited[ny][nx] = True
                for i in range(4):
                    visited[ny + dy[i]][nx + dx[i]] = True

                backtracking(ny, nx)

                # 방문 취소
                arr.pop()
                visited[ny][nx] = False
                for i in range(4):
                    visited[ny + dy[i]][nx + dx[i]] = False


visited = [[False] * N for _ in range(N)]
arr = []
answer = 3001
backtracking(-1, -1)
print(answer)
