from collections import defaultdict

def solve(cafes, m):
    ans = [(0, 0)]
    for i in range(len(cafes)):
        cafes[i][1].sort()
        if ans[-1][1] != cafes[i][1][0]:
            cafes[i][1].sort(reverse = True)
        ans += [(cafes[i][0], j) for j in cafes[i][1]]

    for idx in m:
        print(*ans[idx])

T = int(input())
for _ in range(T):
    # Input
    n = int(input())
    cafes = defaultdict(list)
    for _ in range(n):
        x, y = map(int, input().split())
        cafes[x].append(y)
    m = list(map(int, input().split()))
    # Solve
    solve(sorted(cafes.items()), m[1:])