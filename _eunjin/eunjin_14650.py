from itertools import product

N = int(input())

# 3^9가지  만들고, 3의 배수인 것만 개수 세기
sets = [0, 1, 2]
# data = list()

answer = 0

for nums in product(sets, repeat=N):
    total = 0
    for i in range(N - 1, -1, -1):
        k = nums[i] * 10**(N - 1 - i)
        total += k

    if total < 10**(N - 1):  # 0으로 시작하는 수 거르기
        continue

    if total % 3 == 0:  # 3의 배수만 개수 카운트
        answer += 1

print(answer)

