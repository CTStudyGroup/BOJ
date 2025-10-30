import sys

sys.setrecursionlimit(10**6)
N = int(input())

path = []
def dfs(src, dst, n) :
    if n == 1 :
        path.append([src, dst])
        return
    mid = 6-src-dst
    dfs(src, mid, n-1)
    dfs(src, dst, 1)
    dfs(mid, dst, n-1)

answer = 0

if N <= 20 :
    dfs(1, 3, N)
    print(len(path))
    for a, b in path :
        print(a, b)
else :
    print(2**N - 1)
