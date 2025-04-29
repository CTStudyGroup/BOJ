def solve(n, m, T):
    ans, val = 0, sum(T[:m])
    if n == m:
        return val
    
    for i in range(m, n):
        ans = max(ans, val)
        val += T[i]-T[i-m]
    return max(ans, val)

n, m = list(map(int, input().split()))
T = list(map(int, input().split()))
print(solve(n, m, T))