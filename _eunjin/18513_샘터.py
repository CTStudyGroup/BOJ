import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
arr = list(map(int, input().split()))

visited = set(arr)  # 샘터 위치 방문 처리
q = deque()

# 샘터 좌표부터 탐색 대상
for start in arr:
    q.append((start, 0))  # node, dist

cnt = 0
answer = 0

# bfs
while q and cnt < K:
    curr, dist = q.popleft()

    # 양 옆 좌표 탐색
    for nxt in (curr - 1, curr + 1):
        if nxt not in visited:
            visited.add(nxt)
            q.append((nxt, dist + 1))
            answer += dist + 1
            cnt += 1
            if cnt == K:
                break

print(answer)
