import sys
import math
input = sys.stdin.readline

# 주어진 K보다 큰 소수 - 작은 소수

# 소수인지 여부 미리 전부 구해놓기
MAX = 1299709
is_prime = [True] * (MAX + 1)
is_prime[1] = False  # 1은 소수 아님

for i in range(2, int(math.sqrt(MAX) + 1)):
    if not is_prime[i]:
        continue
    for j in range(2 * i, MAX + 1, i):
        is_prime[j] = False

T = int(input())
for _ in range(T):
    k = int(input())

    if is_prime[k]:
        print(0)
    else:
        start = k
        end = k

        for i in range(k, 0, -1):
            if is_prime[i]:
                start = i
                break

        for i in range(k, MAX + 1):
            if is_prime[i]:
                end = i
                break

        print(end - start)
