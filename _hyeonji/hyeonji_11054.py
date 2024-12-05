import sys
input=sys.stdin.readline

n=int(input())
a=list(map(int,input().split()))

i_d=[1 for i in range(n)]
d_d=[1 for i in range(n)]

for i in range(1,n):
    for j in range(i):
        if a[i]>a[j]:
            i_d[i]=max(i_d[i],i_d[j]+1)

a.reverse()

for i in range(1,n):
    for j in range(i):
        if a[i]>a[j]:
            d_d[i]=max(d_d[i],d_d[j]+1)

d_d.reverse()

result=[]
for i in range(n):
    result.append(i_d[i]+d_d[i]-1)
print(max(result))