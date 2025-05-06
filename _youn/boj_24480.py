from collections import defaultdict, deque

def dfs(E:defaultdict, R:int, N:int):
    stack = deque([R])
    visited = [False for _ in range(N+1)]
    visited[R] = True
    order = [0 for _ in range(N+1)]
    cnt = 1

    while stack:
        u = stack.pop()
        visited[u] = True
        if order[u]==0:
            order[u] = cnt
            cnt += 1

        for v in E[u]:
            if not visited[v]:
                stack.append(v)
    return order[1:]          

# Input
N, M, R = list(map(int, input().split()))
E = defaultdict(list)
for _ in range(M):
    u, v = map(int, input().split())
    E[u].append(v)
    E[v].append(u)

for k in E.keys():
    E[k].sort()
print(*dfs(E, R, N),sep='\n')