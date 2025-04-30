import sys
input = sys.stdin.readline

N, M = map(int, input().split())
T = list(map(int, input().split()))

val = sum(T[:M])
answer = val

for i in range(M, N):
    val = val + T[i] - T[i - M]
    answer = max(answer, val)

print(answer)
