# 입력 받기
N = int(input())

arr = list(map(int, input().split()))

arr = sorted(arr)

result = 0
for i in range(0, N):
    result += arr[i]*(N-i)

print(result)
