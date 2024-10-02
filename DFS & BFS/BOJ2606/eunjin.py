# 입력 받기
N = int(input())  # 컴퓨터의 수
M = int(input())  # 간선의 수

adj_list = [[] for _ in range(N+1)]

for _ in range(M):
    v1, v2 = map(int, input().split())
    adj_list[v1].append(v2)
    adj_list[v2].append(v1)
# print(adj_list)


visited = [False]*(N+1)

# dfs로 탐색 후, visited True의 개수 세기


def dfs(node):
    global visited, adj_list

    if(visited[node]):
        return

    #print("visit node:", node)
    visited[node] = True

    for adj_node in adj_list[node]:
        dfs(adj_node)


dfs(1)
print(sum(visited)-1)
