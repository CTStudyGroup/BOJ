import sys
input=sys.stdin.readline

n=int(input())

info={}
for i in range(n):
    b,p,q,r=map(int,input().split())
    score_mul=p*q*r
    score_sum=p+q+r
    info[b]=[score_mul,score_sum]

sort_info=dict(sorted(info.items(), key=lambda x:(x[1][0],x[1][1],x[0])))

print(*list(sort_info.keys())[:3])