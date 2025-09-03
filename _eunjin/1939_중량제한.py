import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

# A-B 사이 다리가 여러개 있을 수 있음, 다리는 모두 양방향
adj_list = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    adj_list[a].append((b, c))
    adj_list[b].append((a, c))

start, end = map(int, input().split())

# start -> end까지의 다리 최소 무게가 max_value보다 크거나 같은지
def bfs(max_value):
    visited = [False] * (N + 1)
    q = deque()
    q.append(start)

    visited[start] = True

    while q:
        node = q.popleft()
        if node == end:
            return True

        for adj_node, weight in adj_list[node]:
            if not visited[adj_node] and weight >= max_value:
                visited[adj_node] = True
                q.append(adj_node)

    return False

# T T T F F F F
# start -> end로 가는 최단경로 c의 최댓값 찾기
# c값을 1~10^9 사이에서 이분탐색으로 찾아가기
left, right = 0, 10**9 + 1
answer = 0
while left < right:
    mid = (left + right) // 2
    if bfs(mid):
        answer = mid
        left = mid + 1
    else:
        right = mid


print(answer)

