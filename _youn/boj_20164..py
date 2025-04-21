from itertools import combinations

def oddNum(N):
    odds = list(filter(lambda x: int(x)%2==1, list(N)))
    return len(odds)

def solve(N, count):
    if len(N)==1:
        global ans
        ans.append(count)
        return
    elif len(N)==2:
        val = str(int(N[0]) + int(N[1]))
        solve(val, count + oddNum(val))
    else:
        for c in combinations(range(1, len(N)), 2):
            i, j = c
            val = str(int(N[:i]) + int(N[i:j]) + int(N[j:]))
            solve(val, count + oddNum(val))

N = input()
ans = []
solve(N, oddNum(N))
print(min(ans), max(ans))
