import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 1. 입력 및 그래프 구성
N = int(input())
graph = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 2. DP 테이블 선언
# dp[u][0] = u가 얼리어답터가 아닐 때 필요한 최소 얼리어답터 수
# dp[u][1] = u가 얼리어답터일 때 필요한 최소 얼리어답터 수
dp = [[0, 0] for _ in range(N + 1)]
visited = [False] * (N + 1)


# 3. DFS (후위 순회 방식)
def dfs(u):
    visited[u] = True
    dp[u][0] = 0      # 초기값 설정 (u가 얼리X)
    dp[u][1] = 1      # 초기값 설정 (u가 얼리O)

    for v in graph[u]:
        if not visited[v]:
            dfs(v)
            # TODO: 점화식 채워 넣기
            dp[u][0] += dp[v][1]
            dp[u][1] += min(dp[v][0], dp[v][1])
            pass


# 4. 루트(1)에서 시작
dfs(1)

# 5. 정답 출력
print(min(dp[1][0], dp[1][1]))
