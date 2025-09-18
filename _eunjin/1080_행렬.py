import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = [list(map(int, list(input().strip()))) for _ in range(N)]
B = [list(map(int, list(input().strip()))) for _ in range(N)]

# dp, 백트래킹 이런게 아닌거같음..
# 그리디인가

_dict = {}
_dict[1] = 0
_dict[0] = 1

answer = 0
for y in range(N - 2):
    for x in range(M - 2):
        if A[y][x] != B[y][x]:
            for i in range(y, y + 3):
                for j in range(x, x + 3):
                    A[i][j] = _dict[A[i][j]]
            answer += 1


if A == B:
    print(answer)
else:
    print(-1)
