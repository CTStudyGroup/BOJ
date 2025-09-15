from itertools import permutations
N = int(input())

arr = list(map(int, input().split()))

answer = 0
for perm in permutations(arr, N):
    val = 0
    for i in range(N - 1):
        val += abs(perm[i] - perm[i + 1])
    answer = max(answer, val)

print(answer)
