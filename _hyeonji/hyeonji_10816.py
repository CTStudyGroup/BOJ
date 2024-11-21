import sys
input=sys.stdin.readline

n=int(input())
card=list(map(int,input().split()))
m=int(input())
target_card=list(map(int,input().split()))
result=dict()

for i in card:
    if result.get(i)==None:
        result[i]=1
    else:
        result[i]+=1

for i in target_card:
    if result.get(i)==None:
        print(end='0 ')
    else:
        print(result[i],end=" ")