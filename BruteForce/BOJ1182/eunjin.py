from itertools import combinations

# 입력 받기
N, S = map(int, input().split())

arr = list(map(int, input().split()))

comb_list = []

for i in range(N):
    comb_list.extend(list(combinations(arr, i+1)))

# print(comb_list)


result = 0
for comb in comb_list:
    comb_sum = 0
    for elem in comb:
        comb_sum += elem
    if(comb_sum == S):
        result += 1

print(result)
