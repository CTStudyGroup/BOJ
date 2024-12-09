# 입력 받기
N, L = map(int, input().split())

arr = list(map(int, input().split()))

arr.sort()

result = 1
cover = arr[0]+L-1

for i in range(N):
    if arr[i] <= cover:
        continue

    result += 1
    cover = arr[i]+L-1

print(result)
