N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

# 백트래킹으로 가능한 모든 부메랑 조합 탐색

dy = [[0, 0, 1], [-1, 0, 0], [-1, 0, 0], [0, 0, 1]]
dx = [[-1, 0, 0], [0, 0, -1], [0, 0, 1], [1, 0, 0]]

def able(y, x, s):
    for i in range(3):
        ny, nx = y + dy[s][i], x + dx[s][i]

        if ny < 0 or ny >= N or nx < 0 or nx >= M:
            return False

        if visited[ny][nx]:
            return False
    return True

def next_cords(y, x):
    nx = x + 1
    ny = y
    if nx == M:
        nx = 0
        ny += 1
    return ny, nx

def backtracking(cy, cx, score):  # (y,x)를 중심으로 하는 s 모양 부메랑
    global answer
    # print("--- visit cy:", cy, ", cx:", cx, ", score:", score)

    if cy == N:
        answer = max(answer, score)
        return

    # 해당 칸에 부메랑 놓는 경우
    if not visited[cy][cx]:
        for s in range(4):
            if not able(cy, cx, s):
                continue

            temp = 0
            for i in range(3):
                ny, nx = cy + dy[s][i], cx + dx[s][i]
                visited[ny][nx] = True
                if i == 1:
                    temp += matrix[ny][nx] * 2
                else:
                    temp += matrix[ny][nx]

            ny, nx = next_cords(cy, cx)
            backtracking(ny, nx, score + temp)  # 다음 노드 방문

            # 다음 노드 방문 취소 처리
            for i in range(3):
                ny, nx = cy + dy[s][i], cx + dx[s][i]
                visited[ny][nx] = False

    # 해당 칸에 부메랑 안놓는 경우
    ny, nx = next_cords(cy, cx)
    backtracking(ny, nx, score)


visited = [[False] * M for _ in range(N)]
answer = 0

backtracking(0, 0, 0)
print(answer)
