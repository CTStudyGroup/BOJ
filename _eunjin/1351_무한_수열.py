import math

N, P, Q = map(int, input().split())

# A0 = 1
# A1 = A0 + A0 = 2
# A2 = A1 + A0 = 3
# A3 = A1 + A1 = 4
# A4 = A2 + A1 = 5

# dp
A = [0] * (N + 1)
A[0] = 1

for i in range(1, N + 1):
    p = math.floor(i / P)
    q = math.floor(i / Q)
    A[i] = A[p] + A[q]

print(A[N])
