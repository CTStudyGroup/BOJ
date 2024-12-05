import sys
input=sys.stdin.readline

n=int(input())

info=[]
for i in range(n):
    s,e=map(int,input().split())
    info.append([e,s])

info.sort()

answer=0
setting_end=-1
for i in info:
    if i[1]>=setting_end:
        answer+=1
        setting_end=i[0]

print(answer)