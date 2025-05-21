MAX_N = 1000000

def solve(n):
    ans = [1, 0]
    F = [0] * (MAX_N+1)
    F[1] = 1

    if n<0 and abs(n)%2==0: ans[0]=-1
    if n==0: ans[0]=0

    for i in range(2,abs(n)+1):
        F[i] = F[i-1]+ F[i-2] % 1000000000
    ans[1] = F[abs(n)]% 1000000000
    return ans

n = int(input())
print(*solve(n),sep='\n')