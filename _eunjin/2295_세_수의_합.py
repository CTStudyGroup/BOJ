import sys
input = sys.stdin.readline

# 가능한 모든 두 수의 합을 구한 뒤,
# 주어진 수 중 제일 큰 것부터 보면서 (주어진 수 - 특정 하나의 수) 값이 모든 두 수의 합 조합에 있는지 여부

N = int(input())
U = []
for _ in range(N):
    x = int(input())
    U.append(x)
U.sort()

# print(U)

comb = set()
for i in range(N):
    for j in range(i, N):
        comb.add(U[i] + U[j])

# print(comb)

for i in range(N - 1, -1, -1):
    for j in range(N):
        if U[i] - U[j] in comb:
            print(U[i])
            exit()
