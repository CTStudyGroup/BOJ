import math

N = int(input())
is_prime = [True]*(N+1)
is_prime[1] = False

# 소수 구하기
for i in range(2, int(math.sqrt(N))+1):
    if not is_prime[i]:
        continue
    for j in range(2*i, N+1, i):
        is_prime[j] = False

primes = []
for i in range(1, N+1):
    if is_prime[i]:
        primes.append(i)

# print(primes)


if not primes:
    print(0)
    exit()

answer = 0

right = -1
cur_sum = 0
for left in range(len(primes)):
    while (right+1 < len(primes)) and (cur_sum+primes[right+1] <= N):
        right += 1
        cur_sum += primes[right]

    if cur_sum == N:
        answer += 1

    # print("left:", left, ", right:", right, "cur_sum:", cur_sum)
    cur_sum -= primes[left]
    # print("after cur_sum:", cur_sum)
    # print("------------------------------------")

print(answer)
