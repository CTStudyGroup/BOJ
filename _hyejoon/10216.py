import sys
input = sys.stdin.readline

def find(unf, a):
    while unf[a] != a:
        unf[a] = unf[unf[a]]  
        a = unf[a]
    return a

def union(unf, a, b):
    ra = find(unf, a)
    rb = find(unf, b)
    if ra > rb:
        unf[ra] = rb
    else:
        unf[rb] = ra

def is_union(unf, a, b):
    return find(unf, a) == find(unf, b)

def solve(N, camps, unf):
    for i in range(N - 1):
        x1, y1, r1 = camps[i]
        for j in range(i + 1, N):
            x2, y2, r2 = camps[j]
            dx = x1 - x2
            dy = y1 - y2
            if dx * dx + dy * dy <= (r1 + r2) ** 2:
                if not is_union(unf, i, j):
                    union(unf, i, j)

    roots = set(find(unf, i) for i in range(N))
    print(len(roots))


T = int(input())
for _ in range(T):
    N = int(input())
    unf = list(range(N))
    camps = [tuple(map(int, input().split())) for _ in range(N)]
    solve(N, camps, unf)


