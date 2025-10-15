# DP
# DP[i]: i일에 살아있는 짚신 벌레 수.
# 증가만 생각했을 때
# DP[i] = DP[i-1] + DP[i-a]
# i-a에 존재하는 벌레들이 모두 성체가 되어 자식을 낳았다고 가정(늙어서 못낳는 경우는 생각안함)

# 멈춤까지 생각했을때
# DP[i] = DP[i-1] + DP[i-a] - DP[i-b]
# i-a에 존재하는 벌레들이 모두 성체가 됨. (증가)
# DP[i-a]를 모두 더해주는 것은 안됨. why? -> DP[i-a] 때 존재하는 벌레가 이미 나이를 먹은 상태면 DP[i] 때 번식을 못할 수도 있음.

# DP[i-a] - DP[i-b]가 갖는 의미: [i-a] ~ [i-b] 기간동안 새로 생긴 벌레의 수
# 이 기간동안 생긴 벌레가 DP[i] 때 새로운 자식을 낳는다.
# 따라서, DP[i] = DP[i-1] + DP[i-a] - DP[i-b]


import sys 
a, b, d, N = map(int, sys.stdin.readline().split())

def sol(a, b, d, N):
    dp = [0] * (N + 1)

    # 초기화
    for i in range(a):
        dp[i] = 1
    
    # a ~ b 번식
    for i in range(a, N + 1):
        dp[i] = (dp[i - 1] + dp[i - a]) % 1000

        if i >= b:
            dp[i] = (dp[i] - dp[i - b]) % 1000
    
    # 죽은 벌레
    if N >= d: # 에외 처리
        print((dp[N] - dp[N - d]) % 1000)
    else:
        print(dp[N] % 1000)
        
sol(a, b, d, N)