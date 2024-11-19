from math import sqrt

# 입력 받기
M, N = map(int, input().split())


isPrime = [True]*(N+1)
isPrime[1] = False

for i in range(2, int(sqrt(N))+1):
    if not isPrime[i]:
        continue
    for j in range(2*i, N+1, i):
        isPrime[j] = False


for i in range(M, N+1):
    if isPrime[i]:
        print(i)
