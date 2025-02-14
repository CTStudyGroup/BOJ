N = int(input())
levels = list(map(int, input().split()))

max_idx = -1
max_level = 0
for i in range(N):
    if levels[i] > max_level:
        max_idx = i
        max_level = levels[i]

answer = 0

for i in range(0, max_idx):
    answer += levels[i]+levels[max_idx]

for i in range(max_idx+1, N):
    answer += levels[i]+levels[max_idx]

print(answer)
