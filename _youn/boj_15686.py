import sys
from itertools import combinations

def get_distance(home, chicken):
    distance = [[0]*len(chicken) for _ in range(len(home))]
    for i in range(len(home)):
        for j in range(len(chicken)):
            distance[i][j] = abs(home[i][0]-chicken[j][0]) + abs(home[i][1]-chicken[j][1])
    return distance

def solve(home, chicken, M):
    distance = get_distance(home, chicken)
    ans = float('inf')
    for perm in combinations(range(len(chicken)), M):
        val = 0
        for i in range(len(home)):
            tmp = [distance[i][j] for j in perm]
            val += min(tmp)
        ans = min(ans, val)
    return ans

# Input
N, M = map(int, sys.stdin.readline().split())
chicken, home = [], []
for i in range(N):
    tmp = list(map(int, sys.stdin.readline().split()))
    for j in range(N):
        if tmp[j] == 1: home.append((i,j))
        if tmp[j] == 2: chicken.append((i,j))
print(solve(home, chicken, M))