N = int(input())
matrix = []
adj_list = []

for i in range(N):
    cost = list(map(int, input().split()))
    matrix.append(cost)
    adj_node = []
    for j in range(N):
        if cost[j]:
            adj_node.append(j)
    adj_list.append(adj_node)


# print(matrix)
# print(adj_list)


def dfs(node, cost):
    global adj_list, visited, min_cost, start

    if False not in visited:  # 모든 도시를 방문한 경우
        if matrix[node][start]:
            min_cost = min(min_cost, cost+matrix[node][start])

    for adj_node in adj_list[node]:  # 인접 도시 전체에 대해 탐색
        if visited[adj_node]:  # 이미 방문한 도시인 경우
            continue

        temp_cost = cost+matrix[node][adj_node]

        if temp_cost < min_cost:  # 더 짧은 경로인 경우에만 도시 방문
            visited[adj_node] = True
            dfs(adj_node, temp_cost)
            visited[adj_node] = False


INF = 1e6
min_cost = INF*N

for i in range(N):
    visited = [False]*N
    visited[i] = True
    start = i

    dfs(i, 0)

print(min_cost)
