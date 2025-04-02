from itertools import product

def solve(N):
    count = 0
    for p in product([0,1,2], repeat=N):
        if p[0]==0:
            continue
        if sum(p)%3==0:
            count+=1
    print(count)

N = int(input())
solve(N)