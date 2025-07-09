import sys
input = sys.stdin.readline

N, M = map(int, input().split())

arr = list(map(int, input().split()))

# 시간 초과 풀이
# adj_list = [[] for _ in range(N)]  # adj_list[0]=1 : 0->1, 0이 상사

# for i in range(1, N):
#     adj_list[arr[i] - 1].append(i)

# # print(adj_list)

# def bfs(start, w):
#     q = deque()
#     q.append(start)
#     score[start] += w
#     visited = [False] * N
#     visited[start] = True

#     while q:
#         node = q.popleft()
#         next_node = adj_list[node]

#         for next_node in adj_list[node]:
#             if not visited[next_node]:
#                 score[next_node] += w
#                 q.append(next_node)
#                 visited[next_node] = True

# score = [0] * N
# for _ in range(M):
#     i, w = map(int, input().split())
#     bfs(i - 1, w)


# print(*score)

# 상사의 번호는 자신의 번호보다 작다
# dp
# dp[i] = dp[arr[i]]+w, i가 받은 칭찬 크기 = i의 상사가 받은 칭찬 + i 본인이 받은 칭찬

dp = [0] * (N + 1)
dp[1] = 0
for _ in range(M):
    i, w = map(int, input().split())
    dp[i] += w

for i in range(2, N + 1):
    dp[i] += dp[arr[i - 1]]

print(*dp[1:])
