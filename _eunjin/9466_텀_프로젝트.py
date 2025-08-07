# linked list처럼 dfs로 탐색했을 때 사이클이 있어야 팀에 속할 수 있음
# (본인을 지목한 학생)을 지목한 학생은 바로 혼자가 됨

# 틀린 풀이
# # 해당 노드부터 dfs탐색 시작하고, 사이클이 시작되는 노드 반환
# import sys
# input = sys.stdin.readline

# T = int(input())

# def dfs(node):
#     if cycle_visited[node]:
#         return node

#     cycle_visited[node] = True
#     visited[node] = True
#     next_node = selected[node] - 1
#     return dfs(next_node)


# def solve(start):
#     global cycle_visited
#     cycle_visited = [False] * N

#     n = dfs(start)

#     while not isTeam[n]:
#         isTeam[n] = True
#         n = selected[n] - 1

# for _ in range(T):
#     N = int(input())
#     selected = list(map(int, input().split()))

#     visited = [False] * N
#     cycle_visited = []
#     isTeam = [False] * N

#     for i in range(N):
#         if selected[i] == i + 1:  # 자기 자신 선택한 경우
#             isTeam[i] = True

#         if not visited[i]:
#             start = i
#             solve(start)

#     print(N - sum(isTeam))

# 정답 풀이
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

T = int(input())

def dfs(x):
    global count
    visited[x] = True
    path.append(x)
    next = graph[x]

    if not visited[next]:
        dfs(next)
    else:
        if not finished[next]:  # 사이클 발견 → next부터 현재 x까지가 사이클
            cycle_idx = path.index(next)  # 현재까지의 경로에서 사이클 시작 인덱스 찾기
            count -= len(path[cycle_idx:])  # 사이클에 포함된 애들 제외

    finished[x] = True
    path.pop()

for _ in range(T):
    n = int(input())
    graph = [0] + list(map(int, input().split()))  # 1-based
    visited = [False] * (n + 1)  # dfs 탐색 중 방문한 칸인지
    finished = [False] * (n + 1)  # 사이클 여부가 확정되었는지
    count = n
    path = []  # dfs 방문 경로

    for i in range(1, n + 1):
        if not visited[i]:
            dfs(i)

    print(count)
