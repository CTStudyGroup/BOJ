import sys
input = sys.stdin.readline

MAX = 1000000

# 약수의 합 배열
d = [0] * (MAX + 1)

# d[i] = i의 모든 약수의 합
for i in range(1, MAX + 1):
    for j in range(i, MAX + 1, i):
        d[j] += i

# g[n] = d[1] + d[2] + ... + d[n]
g = [0] * (MAX + 1)
for i in range(1, MAX + 1):
    g[i] = g[i - 1] + d[i]

T = int(input())
for _ in range(T):
    n = int(input())
    print(g[n])
