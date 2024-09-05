from itertools import combinations
import sys
input=sys.stdin.readline

l,c=map(int,input().split())
info=list(input().rstrip().split())

info.sort()   # 정렬
case=list(combinations(info,l))   # abc : o, bac : x (문제조건)

v=['a','e','i','o','u']

for i in case:
    cnt_c=0    # 자음 개수
    cnt_v=0    # 모음 개수
    for j in i:
        if j in v:
            cnt_v+=1
        else:
            cnt_c+=1
    if cnt_v>=1 and cnt_c>=2:    # 최소 한 개의 모음 + 최소 두 개의 자음.
        print(''.join(list(i)))