cypher = list(map(int, input().strip()))
dp = [0]*(len(cypher)+1)
dp[0], dp[1] = 1, 1

if cypher[0]==0: print(0)
else:
    for i in range(1, len(cypher)):
        idx = i + 1
        if cypher[i] > 0:
            dp[idx] += dp[idx-1]
        if 10 <= cypher[i-1]*10+cypher[i] <= 26:
            dp[idx] += dp[idx-2]
        dp[i]%=1000000
    print(dp[-1]%1000000)