N = int(input())

num = list(map(int, input().split()))

if N == 1:
    print(sum(num) - max(num))
    exit()

d3 = [(3, 4, 5), (2, 4, 5), (1, 2, 5), (1, 3, 5), (3, 4, 0), (2, 4, 0), (1, 2, 0), (1, 3, 0)]
d2 = [(3, 4), (2, 4), (1, 2), (1, 3), (0, 3), (0, 4), (0, 2), (0, 1), (5, 3), (5, 4), (5, 2), (5, 1)]

# 3면의 최솟값
min3 = 1e9
for x, y, z in d3:
    temp = num[x] + num[y] + num[z]
    min3 = min(min3, temp)

# 2면의 최솟값
min2 = 1e9
for x, y in d2:
    temp = num[x] + num[y]
    min2 = min(min2, temp)

min1 = min(num)

# 탁자x
answer = min3 * 4 + min2 * 8 * (N - 2) + min1 * 5 * (N - 2)**2

# 탁자o
answer += min2 * 4 + min1 * 4 * (N - 2)

print(answer)
