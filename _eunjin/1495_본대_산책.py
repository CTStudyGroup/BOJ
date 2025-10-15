adj_list = [[] for _ in range(8)]

vertex = [(0, 2), (0, 1), (1, 3), (2, 3), (2, 4), (3, 4), (3, 5),
          (4, 5), (4, 6), (5, 6), (5, 7), (6, 7)]

for v in vertex:
    adj_list[v[0]].append(v[1])
    adj_list[v[1]].append(v[0])


D = int(input())
MOD = 1000000007

# dp[y][x]: y분동안 걷고 현재 위치가 x번 노드일 경로의 수
dp = [[0] * 8 for _ in range(D + 1)]
dp[0][7] = 1

# 이전 시점에 경로를 가진 노드 -> 현재 시점에 인접 노드로 경로 전파
for i in range(1, D + 1):
    for j in range(8):
        for adj_node in adj_list[j]:
            dp[i][adj_node] = (dp[i][adj_node] + dp[i - 1][j]) % MOD

print(dp[D][7])
