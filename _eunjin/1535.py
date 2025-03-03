from itertools import combinations

N = int(input())
minus = list(map(int, input().split()))
plus = list(map(int, input().split()))

mx = 0

for n in range(1, N + 1):
    for comb in combinations(range(0, N), n):
        hp = 100
        point = 0
        for i in comb:
            if hp - minus[i] <= 0:
                point = 0
                break
            hp -= minus[i]
            point += plus[i]
        mx = max(mx, point)

print(mx)
