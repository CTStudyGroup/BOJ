import sys
input = sys.stdin.readline

N, M, H = map(int, input().split())
blocks = [list(map(int, input().split())) for _ in range(N)]
MOD = 10007

_set = set()

def backtracking(I, h):
    if h == H:
        _set.add(tuple(used))
        return

    for i in range(N):
        if not used[i]:
            for block in blocks[i]:
                if h + block <= H:
                    h += block
                    used[i] = block
                    backtracking(i, h)
                    h -= block
                    used[i] = 0

used = [0] * N

backtracking(0, 0)
print(len(_set) % MOD)
