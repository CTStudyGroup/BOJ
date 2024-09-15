import sys
input=sys.stdin.readline

n,k=map(int,input().split())  # n : 동전 종류의 개수, k : 가치의 합

value=[]
for i in range(n):
    value.append(int(input()))

value.sort(reverse=True)

cnt=0                # 동전 개수
for i in value:
    if k==0:
        break
    cnt+=k//i
    k=k%i

print(cnt)