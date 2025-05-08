from collections import deque

def dfs(start, friends, N):
    stack = deque([(start, 0, {start})])
    while stack:
        u, depth, visited = stack.pop()
        if depth>=4:
            return 1
        for v in friends[u]:
            if v not in visited:
                stack.append((v, depth+1, visited | {v}))
    return 0

# Input
N, M = map(int, input().split())
friends = {i:[] for i in range(N)}
for _ in range(M):
    a, b = map(int, input().split())
    friends[a].append(b)
    friends[b].append(a)
# Solve
ans = 0
for i in range(N):
    ans = ans | dfs(i, friends, N)
    if ans == 1: break
print(ans)