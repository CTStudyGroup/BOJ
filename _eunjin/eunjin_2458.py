N, M = map(int, input().split())

s_adj_list = [[] for _ in range(N+1)]  # s_adj_list[1] = [2] : 1번이 2번보다 작다
l_adj_list = [[] for _ in range(N+1)]  # l_adj_list[3] = [4] : 3번이 4번보다 크다

for _ in range(M):
    a, b = map(int, input().split())
    s_adj_list[a].append(b)
    l_adj_list[b].append(a)


def s_dfs(node):
    global s_visited

    if s_visited[node]:
        return

    s_visited[node] = True

    for adj_node in s_adj_list[node]:
        s_dfs(adj_node)


def l_dfs(node):
    global l_visited

    if l_visited[node]:
        return

    l_visited[node] = True

    for adj_node in l_adj_list[node]:
        l_dfs(adj_node)


# 모든 학생에 대해 작은 방향, 큰 방향 각각 dfs해서 거쳐간 노드의 개수 세기
answer = 0

for i in range(1, N+1):
    s_visited = [False]*(N+1)
    l_visited = [False]*(N+1)

    s_dfs(i)
    l_dfs(i)
    if sum(s_visited)+sum(l_visited) == N+1:
        answer += 1

print(answer)
