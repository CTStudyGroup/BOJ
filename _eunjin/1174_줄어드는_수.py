from itertools import combinations

N = int(input())

total = []
for n in range(1, 11):
    for comb in combinations(range(0, 10), n):
        temp = 0
        for i in range(len(comb)):
            temp += comb[i] * 10**i
        total.append(temp)
        # print(temp)

total.sort()

if N > len(total):
    print(-1)
else:
    arr = total[N - 1]
    print(arr)
