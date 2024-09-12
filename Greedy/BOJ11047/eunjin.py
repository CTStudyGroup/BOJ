# 입력 받기
N, K = map(int, input().split())

arr = []

for _ in range(N):
    arr.append(int(input()))

cnt = 0
for i in range(len(arr)-1, -1, -1):
    cnt += K//arr[i]
    K %= arr[i]

print(cnt)
