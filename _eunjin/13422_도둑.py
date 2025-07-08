import sys
input = sys.stdin.readline

def solve(house):
    ret = 0
    curr = sum(house[:M])

    if M == N:
        return 1 if curr < K else 0

    if curr < K:
        ret += 1

    for i in range(1, N):
        # i-1번째 값을 빼고, i+M번째 값을 더함
        curr = curr - house[i - 1] + house[(i - 1 + M) % N]
        if curr < K:
            ret += 1
    return ret

T = int(input())
for _ in range(T):
    N, M, K = map(int, input().split())
    house = list(map(int, input().split()))

    print(solve(house))
