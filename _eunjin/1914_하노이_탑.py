N = int(input())

def dfs(start, dest, n):
    if n == 1:
        print(start, dest)
        return

    mid = 6 - start - dest
    dfs(start, mid, n - 1)
    dfs(start, dest, 1)
    dfs(mid, dest, n - 1)

path = []
print(2**N - 1)
if N <= 20:
    dfs(1, 3, N)
