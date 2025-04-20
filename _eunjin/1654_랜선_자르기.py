import sys
input = sys.stdin.readline

K, N = map(int, input().split())
length = [int(input()) for _ in range(K)]

# 랜선의 길이를 n으로 설정하면 N개의 조각이 나오는지 여부
def able(n):
    cnt = 0
    for x in length:
        cnt += x // n
    return cnt >= N

left = 1
right = 2**31 - 1
ans = -1

while left <= right:
    mid = (left + right) // 2

    if able(mid):
        left = mid + 1
        ans = mid
    else:
        right = mid - 1


print(ans)
