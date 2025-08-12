import sys
input = sys.stdin.readline

rows, cols = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(rows)]

shapes = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
visited = [[0] * cols for _ in range(rows)]

def boo(centerX, centerY):
    if centerY == rows:
        return 0

    # 다음 좌표
    nextX, nextY = (centerX + 1, centerY) if centerX + 1 < cols else (0, centerY + 1)

    # 1) 부메랑 안 놓고 넘어가는 경우
    maximum = boo(nextX, nextY)

    # 2) 부메랑 놓는 경우
    for dx, dy in shapes:
        nx, ny = centerX + dx, centerY + dy

        if 0 <= nx < cols and 0 <= ny < rows:
            if not visited[centerY][centerX] and not visited[ny][centerX] and not visited[centerY][nx]:
                total = matrix[centerY][centerX] * 2 + matrix[ny][centerX] + matrix[centerY][nx]
                # 방문 처리
                visited[centerY][centerX] = visited[ny][centerX] = visited[centerY][nx] = 1
                maximum = max(maximum, total + boo(nextX, nextY))
                # 방문 해제
                visited[centerY][centerX] = visited[ny][centerX] = visited[centerY][nx] = 0

    return maximum

print(boo(0, 0))
