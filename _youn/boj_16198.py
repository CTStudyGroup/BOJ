def solve(N, W, val):
    if len(W) == 2:
        global ans
        ans = max(ans, val)
        return

    for idx in range(1, N-1):
        tmpW = W[:idx] + W[idx+1:]
        solve(N-1, tmpW, val+W[idx-1]*W[idx+1])
        
N = int(input())
W = list(map(int, input().split()))
ans = 0

solve(N, W, 0)
print(ans)