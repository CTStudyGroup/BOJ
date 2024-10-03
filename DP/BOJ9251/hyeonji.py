import sys
input=sys.stdin.readline

a=input().rstrip()
b=input().rstrip()

d=[0 for i in range(1000)]

for i in range(len(a)):
    tmp=0
    for j in range(len(b)):
        if tmp<d[j]:
            tmp=d[j]
        else:
            if a[i]==b[j]:
                d[j]=tmp+1

print(max(d))