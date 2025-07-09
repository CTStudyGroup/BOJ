from collections import deque
from collections import defaultdict
import sys
input = sys.stdin.readline

N, T = map(int, input().split())

# dp??
# dp가 아니다........

_dict = defaultdict(list)
for i in range(N):
    x, y = map(int, input().split())
    _dict[y].append((x, i + 1))


visited = [False] * (N + 1)
q = deque()
q.append((0, 0, 0, 0))  # y,x,n(홈 번호),d
visited[0] = True

while q:
    cy, cx, n, d = q.popleft()
    if cy == T:
        print(d)
        exit()

    for y in range(cy - 2, cy + 3):
        for x, i in _dict[y]:
            if cx - 2 <= x <= cx + 2:
                if not visited[i]:
                    q.append((y, x, i, d + 1))
                    visited[i] = True

print(-1)
