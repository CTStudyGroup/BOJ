import sys
input = sys.stdin.readline

N, C = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

# 1개짜리 확인
for a in arr:
    if a == C:
        print(1)
        exit()

# 2개짜리 확인 -> 투 포인터
left, right = 0, N - 1
while left < right:
    s = arr[left] + arr[right]
    if s == C:
        print(1)
        exit()
    elif s < C:
        left += 1
    else:
        right -= 1

# 3개짜리 확인 -> 1개 고정 + 투 포인터
for i in range(N - 2):
    left, right = i + 1, N - 1
    while left < right:
        s = arr[i] + arr[left] + arr[right]
        if s == C:
            print(1)
            exit()
        elif s < C:
            left += 1
        else:
            right -= 1

print(0)
