N = int(input())
heights = list(map(int, input().split()))

arrows = [0] * (max(heights) + 1)

cnt = 0

for height in heights:
    if arrows[height]:
        arrows[height] -= 1
    else:
        cnt += 1
    if height > 1:
        arrows[height - 1] += 1

# print(arrows)
print(cnt)
