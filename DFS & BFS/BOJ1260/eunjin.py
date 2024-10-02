from collections import deque

# 입력 받기
N, M, V = map(int, input().split())

adj_list = [[] for _ in range(N+1)]

for _ in range(M):
    v1, v2 = map(int, input().split())
    adj_list[v1].append(v2)
    adj_list[v2].append(v1)

# print(adj_list)

dfs_visited = [False]*(N+1)


def dfs(node):
    global adj_list, dfs_visited

    if(dfs_visited[node]):
        return

    dfs_visited[node] = True
    print(node, end=" ")

    for adj_node in sorted(adj_list[node]):
        dfs(adj_node)


def bfs(start):
    q = deque()

    q.append(start)
    bfs_visited = [False]*(N+1)
    bfs_visited[start] = True
    while q:
        node = q.popleft()
        print(node, end=" ")

        for adj_node in sorted(adj_list[node]):
            if(bfs_visited[adj_node]):
                continue
            q.append(adj_node)
            bfs_visited[adj_node] = True


dfs(V)
print()
bfs(V)
