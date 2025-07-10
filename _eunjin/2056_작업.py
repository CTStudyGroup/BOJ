import sys
input = sys.stdin.readline

N = int(input())

# 이거 dfs로 안되나??
# 안된다..
# 작업 동시 수행 가능, A->B 라고 해서 A 방문 후 바로 B 방문할 수 있는게 아님
# B의 모든 선행 작업이 끝나야만 B 방문 가능

# i의 작업 수행 시간 = max(i의 모든 선행 작업의 수행 시간) + i 본인 작업 수행 시간

dp = [0] * (N + 1)

for i in range(1, N + 1):
    arr = list(map(int, input().split()))
    T = arr[0]
    M = arr[1]
    pre = arr[2:]  # 사전 작업 번호

    for p in pre:
        dp[i] = max(dp[i], dp[p])

    dp[i] += T

print(max(dp))
