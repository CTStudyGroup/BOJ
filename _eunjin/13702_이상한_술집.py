import sys
input = sys.stdin.readline

N, K = map(int, input().split())
capacity = list(int(input()) for _ in range(N))

# 답이 될 수 있는 막걸리 용량 범위: 0 ~ 2^31-1 => 이분탐색

# 막걸리 용량을 x로 둘 때, 분배 가능한 사람 수 반환
def count(x):
    cnt = 0
    for c in capacity:
        cnt += c // x

    return cnt

# 이분 탐색
start = 0
end = 2**31 - 1
answer = 0

while start <= end:
    mid = (start + end) // 2
    cnt = count(mid)

    if cnt >= K:  # 분배 가능한 사람 수가 많으므로 탐색 구간을 더 큰 구간으로 좁히기
        start = mid + 1
        answer = mid
    else:  # 분배 가능한 사람 수가 적으므로 탐색 구간을 더 작은 구간으로 좁히기
        end = mid - 1

print(answer)
