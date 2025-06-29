import sys
input = sys.stdin.readline

N, K = map(int, input().split())
codes = list((input().strip() for _ in range(N)))
A, B = map(int, input().split())

# 각 노드에 대해 해밍 거리가 1인 노드 미리 계산
hamming = [[] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if i == j:
            continue

        cnt = 0
        for k in range(K):
            if codes[i][k] != codes[j][k]:
                cnt += 1

        if cnt == 1:
            hamming[i].append(j)


# dfs로 탐색하면서 현재 노드 기준 해밍 거리가 1인 애들만 다음 탐색 대상 노드로 삼음
# B노드에 도착하면 즉시 경로 출력
# 탐색 다 해도 B노드 도착 못하면 -1 출력

def dfs(node):
    global arr
    if node == B - 1:
        print(' '.join(map(str, arr)))
        exit()
        return

    for adj_node in hamming[node]:
        if not visited[adj_node]:
            visited[adj_node] = True
            arr.append(adj_node + 1)
            dfs(adj_node)
            visited[adj_node] = False
            arr.pop()

visited = [False] * N
arr = [A]
dfs(A - 1)
print(-1)
