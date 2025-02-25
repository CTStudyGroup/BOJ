N, M, H = map(int, input().split())
matrix = [[False]*N for _ in range(H)]  # 사다리

for _ in range(M):
    a, b = map(int, input().split())
    matrix[a-1][b-1] = True


def valid():  # i번째가 i번에 도착하는지 여부
    for start in range(N):
        curr = start
        for j in range(H):
            if matrix[j][curr]:  # 오른쪽 이동
                curr += 1
            elif curr > 0 and matrix[j][curr-1]:  # 왼쪽 이동
                curr -= 1
        if curr != start:  # 시작위치와 현재 위치가 다르면
            return False
    return True


def dfs(cnt, x, y):
    global answer
    if valid():
        answer = min(answer, cnt)
        return
    elif cnt == 3 or answer <= cnt:  # 횟수가 3번 이상인 경우
        return

    for i in range(x, H):
        if i == x:
            curr = y
        else:
            curr = 0

        for j in range(curr, N-1):
            if not matrix[i][j] and not matrix[i][j+1]:
                if j > 0 and matrix[i][j-1]:
                    continue
                matrix[i][j] = True
                dfs(cnt+1, i, j+2)
                matrix[i][j] = False


answer = 4
dfs(0, 0, 0)
print(answer if answer < 4 else -1)
