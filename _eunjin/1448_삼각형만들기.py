import sys
input = sys.stdin.readline

N = int(input())
arr = list(int(input()) for _ in range(N))

# 그리디
# 가장 긴 변 < 나머지 두 변의 합

# 오름차순으로 3개 연달아서 보기?
arr.sort()

answer = -1
for i in range(N - 2):
    if arr[i] + arr[i + 1] > arr[i + 2]:
        answer = sum(arr[i:i + 3])

print(answer)
