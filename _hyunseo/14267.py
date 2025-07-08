import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().split())
tree = list(map(int, input().split()))

children = [[] for _ in range(n+1)]
for i in range(2, n+1):
    parent = tree[i-1]
    children[parent].append(i)

compliments = [0] * (n+1)

for _ in range(m):
    i, w = map(int, input().split())
    compliments[i] += w

def dfs(node):
    for child in children[node]:
        compliments[child] += compliments[node]
        dfs(child)

dfs(1)

print(*compliments[1:])
