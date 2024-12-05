import sys
input=sys.stdin.readline

n=int(input())
arr=[]

for i in range(n):
    info=list(map(int,input().split()))
    arr.append(info)

result=[]
for i in range(n):
    cnt=0
    for j in range(n):
        if arr[i][0]<arr[j][0] and arr[i][1]<arr[j][1]:
            cnt+=1
    result.append(cnt+1)

print(*result)