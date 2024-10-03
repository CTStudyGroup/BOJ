N= int(input())
arr=[0] + list(map(int,input().split()))

dp=[-1 for _ in range(N+1)]

dp[1]=1

for n in range(2,N+1):
	best=0
	for i in range(1,n):
		if arr[n]>arr[i]:
			best=max(best,dp[i])
	dp[n]=best+1

print(max(dp[1:]))

