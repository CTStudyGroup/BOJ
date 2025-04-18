from itertools import combinations

def getCombination(M, values, c):
    if M==0:
        global ans
        ans.add(tuple(sorted(c)))
        return
    
    for idx, v in enumerate(values):
        tmp = values[:idx] + values[idx+1:]
        getCombination(M-1, tmp, c+[v])

def solve1(M, values):
    global ans
    for c in combinations(values, M):
        ans.add(tuple(sorted(c)))
        
    for a in sorted(ans):
        print(*a)

def solve2(M, values):
    getCombination(M, values, [])
    for a in sorted(ans):
        print(*a)

N, M = map(int, input().split())
values = list(map(int, input().split()))
ans = set()
solve1(M, values)
# solve2(M, values)