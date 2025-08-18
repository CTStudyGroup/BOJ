import sys

input = sys.stdin.readline


N = int(input())
honey = list(map(int, input().split()))
s = sum(honey)

# 누적합 배열
P = [0] * N
P[0] = honey [0]
for i in range(1, N ):
    P[i] = P[i-1] + honey[i]
s = P[-1]
a = 0
for i in range(1, N-1) :
    a = max( a, s*2 - honey[0] - honey[i] - P[i])
b = 0
for i in range(1, N-1) :
    b = max( b, s - honey[-1] - honey[i] + P[i-1])
c = 0

for i in range(1, N) :
    c = max(c, s + honey[i]-honey[0]-honey[-1])
print(max(a, b, c))

