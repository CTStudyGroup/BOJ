import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)

n,m=map(int,input().split())
arr=[]

def dfs(v):
    if len(arr)==m:
        print(" ".join(map(str,arr)))
        return
    for i in range(v,n+1):
        if i not in arr:
            arr.append(i)
            dfs(i)
            arr.pop()

dfs(1)