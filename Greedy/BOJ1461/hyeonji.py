import sys
input=sys.stdin.readline

n,m=map(int,input().split())
info=list(map(int,input().split()))

p=[]
n=[]
for i in info:
    if i<0:
        n.append(i)
    else:
        p.append(i)

d=[]

n.sort()
for i in range(len(n)//m):
    d.append(abs(n[i*m]))
if len(n)%m!=0:
    d.append(abs(n[(len(n)//m)*m]))

p.sort(reverse=True)
for i in range(len(p)//m):
    d.append(p[i*m])
if len(p)%m!=0:
    d.append(p[(len(p)//m)*m])

d.sort()

result=0
for i in range(len(d)-1):
    result+=(2*d[i])

result+=d[-1]

print(result)