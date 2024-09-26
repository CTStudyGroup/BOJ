import sys
input=sys.stdin.readline

n=int(input())  # 수열 A의 크기
A=list(map(int,input().split()))  # 수열 A

d=[1 for i in range(n)]

# LIS 알고리즘 수행.
for i in range(1,n):
    for j in range(i):
        if A[j]<A[i]:
            d[i]=max(d[i],d[j]+1)

print(max(d))