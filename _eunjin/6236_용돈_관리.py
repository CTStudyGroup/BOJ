import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(int(input()) for _ in range(N))


# 이분탐색?
left = max(arr)
right = sum(arr)  # 한번에 전체 금액 뽑는 경우

while left <= right:
    mid = (left + right) // 2

    out = mid  # 인출 금액
    cnt = 1  # 인출 횟수

    for n in arr:
        if n > out:  # 다시 인출
            cnt += 1
            out = mid
        out -= n  # 사용

    if cnt > M:
        left = mid + 1
    else:
        right = mid - 1

print(mid)
