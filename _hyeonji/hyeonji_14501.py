import sys
input=sys.stdin.readline

n=int(input())
d=[0 for i in range(n+1)]

info=[]
for i in range(n):
    info.append(list(map(int,input().split())))

profit=0
for i in range(n):
    profit=max(profit,d[i])
    if i+info[i][0]>n:
        continue

    d[i+info[i][0]]=max(profit+info[i][1],d[i+info[i][0]])

print(max(d))