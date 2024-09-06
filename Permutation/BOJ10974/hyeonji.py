from itertools import permutations
import sys
input=sys.stdin.readline

n=int(input())

num=[]
for i in range(1,n+1):
    num.append(i)

case=list(permutations(num,n))
for i in case:
    for j in list(i):
        print(j, end=' ')
    print()