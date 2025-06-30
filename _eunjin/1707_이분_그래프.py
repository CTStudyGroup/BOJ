from collections import deque
import sys
input = sys.stdin.readline

T = int(input())

# 이분 그래프???
# 자신과 인접한 노드의 색이 자신의 색과 다른 그래프

def bfs(start):
    q = deque()
    q.append(start)
    visited[start] = 1  # 1번 색 칠함

    while q:
        node = q.popleft()

        for adj_node in adj_list[node]:
            if visited[adj_node]:  # 인접 노드에 색이 칠해져있는 경우
                if visited[node] == visited[adj_node]:
                    return False
            else:  # 인접 노드 아직 색 안칠한 경우, 자신과 다른 색으로 칠하기
                if visited[node] == 1:
                    visited[adj_node] = 2
                else:
                    visited[adj_node] = 1

                q.append(adj_node)

    return True


for _ in range(T):
    V, E = map(int, input().split())
    adj_list = [[] for _ in range(V)]

    for _ in range(E):
        u, v = map(int, input().split())
        adj_list[u - 1].append(v - 1)
        adj_list[v - 1].append(u - 1)

    visited = [0] * V
    for v in range(V):
        if not visited[v]:
            ret = bfs(v)

            if ret == False:
                print("NO")
                break

    if ret:
        print("YES")
