# 입력 받기
N = int(input())

arr = [int(input()) for _ in range(N)]

arr.sort()
value = 0

for i in range(N):
    if(arr[i]*(N-i) > value):
        value = arr[i]*(N-i)


print(value)
