from math import sqrt

MAX = 1000
is_prime = [True] * (MAX + 1)
is_prime[1] = False

for i in range(2, int(sqrt(MAX)) + 1):
    if not is_prime[i]:
        continue
    for j in range(2 * i, MAX + 1, i):
        is_prime[j] = False

prime = []
for i in range(2, MAX + 1):
    if is_prime[i]:
        prime.append(i)


# 1000보다 작은 모든 소수 구하기 = 168개

def backtracking(n, depth):
    global printed
    if depth == 3:
        if n == K:
            print(*sorted(arr))
            printed = True
        return

    for p in prime:
        if n + p > K:
            continue
        if printed:
            continue
        arr.append(p)
        backtracking(n + p, depth + 1)
        arr.pop()


T = int(input())
for _ in range(T):
    K = int(input())
    arr = []
    printed = False
    backtracking(0, 0)
