import sys
from collections import deque
input = sys.stdin.readline

# 3x3 퍼즐의 상하좌우 이동
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 입력받은 3x3 숫자들을 문자열로 변환
start = ''.join(sum([input().split() for _ in range(3)], []))

# BFS 탐색
def bfs(start):
    goal = "123456780"
    visited = {start: 0}
    q = deque([start])

    while q:
        now = q.popleft()

        if now == goal:
            return visited[now]

        zero_idx = now.index('0')
        x, y = divmod(zero_idx, 3)

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < 3 and 0 <= ny < 3:
                n_idx = nx * 3 + ny
                # 문자열 내에서 0과 교환
                lst = list(now)
                lst[zero_idx], lst[n_idx] = lst[n_idx], lst[zero_idx]
                nxt = ''.join(lst)

                if nxt not in visited:
                    visited[nxt] = visited[now] + 1
                    q.append(nxt)
    return -1


print(bfs(start))
