N=int(input())
cost=[[0,0,0]]
cost+=[list(map(int,input().split())) for _ in range(N)]

dp=[[0,0,0] for _ in range(N+1)]

# 초기값 처리
dp=[[0,0,0] for _ in range(N+1)]

# DP Table 갱신
for i in range(1,N+1):
	for j in range(3):
		best=9999
		for k in range(3):
			if(k!=j):
				best = min(best,dp[i-1][k])
		dp[i][j]=cost[i][j]+best

print(min(dp[N][0],dp[N][1],dp[N][2]))