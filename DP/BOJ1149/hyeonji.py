import sys
input=sys.stdin.readline

n=int(input())
d=[[0,0,0] for i in range(n+1)]

for i in range(1,n+1):
    r,g,b=map(int,input().split())
    d[i][0]=min(d[i-1][1],d[i-1][2])+r
    d[i][1]=min(d[i-1][0],d[i-1][2])+g
    d[i][2]=min(d[i-1][0],d[i-1][1])+b

print(min(d[-1]))