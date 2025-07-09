import sys
from collections import defaultdict, deque

input = sys.stdin.readline

n, T = map(int, input().split())

board = []
grid = defaultdict(list)
block_size = 3

for _ in range(n):
    x, y = map(int, input().split())
    board.append((x, y))
    
    gx = x // block_size
    gy = y // block_size
    grid[(gx, gy)].append((x, y))

visited = set()
q = deque()
q.append((0, 0, 0))   # (x, y, cnt)

answer = float('inf')

while q:
    x, y, cnt = q.popleft()

    if y == T:
        print(cnt)
        exit()

    # 현재 블록 좌표
    bx = x // block_size
    by = y // block_size

    # 주변 9개의 블록만 검사
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            nbx = bx + dx
            nby = by + dy

            for a, b in grid.get((nbx, nby), []):
                if abs(a - x) <= 2 and abs(b - y) <= 2:
                    if (a, b) not in visited:
                        visited.add((a, b))
                        q.append((a, b, cnt + 1))

print(-1)
