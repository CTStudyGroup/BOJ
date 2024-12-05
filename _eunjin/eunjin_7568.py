# 입력 받기
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
rate = []

# print(arr)

for i in range(N):
    cnt = 0
    for j in range(N):
        if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
            cnt += 1
    rate.append(cnt+1)


print(' '.join(map(str, rate)))
