from itertools import permutations

def simulate(order):
    score = 0
    batter_idx = 0
    for inning in innings:
        out = 0
        base = [0, 0, 0]
        while out<3:
            in_idx = order[batter_idx]
            result = inning[in_idx]

            if result == 0: # 아웃
                out+=1
            elif result == 4: # 홈런
                score += sum(base) + 1
                base = [0, 0, 0]
            else: # 안타, 2루타, 3루타
                base = [0] * (result-1) + [1] + base
                score += sum(base[3:])
                base = base[:3]

            batter_idx = (batter_idx + 1) % 9
    return score

N = int(input())
innings = [list(map(int, input().split())) for _ in range(N)]
score = 0
for p in permutations(range(1,9)): # 타순
    order = list(p[:3]) + [0] + list(p[3:])
    score = max(score, simulate(order))
print(score)