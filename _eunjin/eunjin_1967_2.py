import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

N = int(input())


def dfs(node, d):
    global adj_list, node_result

    if visited[node]:
        return
    visited[node] = True

    for adj_node in adj_list[node]:
        if not visited[adj_node[0]]:
            node_result.append((adj_node[0], d+adj_node[1]))
            dfs(adj_node[0], d+adj_node[1])


adj_list = [[] for _ in range(N+1)]
for _ in range(N-1):
    p, c, d = map(int, input().split())
    adj_list[p].append((c, d))
    adj_list[c].append((p, d))

if N == 1:
    print(0)
    exit()

# 부모로부터 가장 먼 노드 찾기
visited = [False]*(N+1)
node_result = []

dfs(1, 0)
# print(node_result)

sorted_arr = sorted(node_result, key=lambda x: -x[1])
start_node = sorted_arr[0][0]  # 부모로부터 가장 먼 노드

# 그 노드로부터 가장 먼 노드까지의 거리 찾기
visited = [False]*(N+1)
node_result = []

dfs(start_node, 0)
# print(node_result)

sorted_arr = sorted(node_result, key=lambda x: -x[1])
dist = sorted_arr[0][1]
print(dist)
