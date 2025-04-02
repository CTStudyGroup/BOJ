from itertools import permutations

X = input()
N = int(X)
L = len(X)

# X는 최대 6자리
# 각 자리별 숫자로 만들 수 있는 모든 수 조합 만들고 X보다 큰 수 중에서 최솟값 출력

arr = list(map(int, X))
perms = list(permutations(arr, L))
perms.sort(reverse=True)

numbers = []
for perm in perms:
    num = 0
    for i in range(L):
        num += perm[i] * 10**(L - i - 1)

    if num > N:
        numbers.append(num)
    else:
        break

print(numbers[-1]) if numbers else print(0)
