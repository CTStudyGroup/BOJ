from itertools import combinations
from itertools import permutations
import sys
input=sys.stdin.readline

n=int(input())

arr=[]
for i in range(n):
    arr.append(list(map(int,input().split())))

num=[]
for i in range(1,n+1):
    num.append(i)

comb_num=list(combinations(num,len(num)//2))
comb_num=comb_num[:len(comb_num)//2]

case=[]
for i in comb_num:
    num1=num.copy()
    for j in i:
        num1.remove(j)
    case.append([list(i),num1])

answer=[]
for i in case:
    power = []
    for j in i:
        case1=list(permutations(j,2))
        summ=0
        for k in case1:
            summ+=arr[k[0]-1][k[1]-1]
        power.append(summ)
    answer.append(abs(power[0]-power[1]))

print(min(answer))