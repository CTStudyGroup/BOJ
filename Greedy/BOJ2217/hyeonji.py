import sys
input=sys.stdin.readline

n=int(input())

w=[]
for i in range(n):
    w.append(int(input()))

w.sort(reverse=True)

rope=[0]+w[:]

answer=0
for i in range(1,n+1):
    answer=max(answer,rope[i]*i)

print(answer)
