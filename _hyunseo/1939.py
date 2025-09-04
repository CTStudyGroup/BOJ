import sys
from collections import defaultdict, deque

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

# N개의 섬, M개의 다리
N, M = map(int, input().split())
bridge = defaultdict(list)
max_weight = 0

for _ in range(M):
    a, b, c = map(int, input().split())
    bridge[a].append((b, c))
    bridge[b].append((a, c))
    max_weight = max(max_weight, c)

start, end = map(int, input().split())

# BFS로 weight_limit 이상 다리를 따라 end까지 도달 가능한지 확인
def possible(weight_limit):
    visited = [0] * (N + 1)
    q = deque([start])
    visited[start] = 1
    
    while q:
        curr = q.popleft()
        if curr == end:
            return True
        for nei, cost in bridge[curr]:
            if not visited[nei] and cost >= weight_limit:
                visited[nei] = 1
                q.append(nei)
    return False

# 이분탐색: 최대 중량 찾기
lo, hi = 1, max_weight
answer = 0

while lo <= hi:
    mid = (lo + hi) // 2
    if possible(mid):
        answer = mid  # mid 가능하면 더 큰 값도 확인
        lo = mid + 1
    else:
        hi = mid - 1

print(answer)
