
def t(n) :
    global dp
    if dp[n] != 0 :
        return dp[n]
    
    answer = 0
    for i in range(n) :
        answer += t(i)*t(n-i-1)
    dp[n] = answer
    return dp[n]

N = int(input())
dp = [0]*36
dp[0] = 1
print(t(N))
