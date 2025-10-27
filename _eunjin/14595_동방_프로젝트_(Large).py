import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

if M == 0:
    print(N)
    sys.exit()

intervals = []
for _ in range(M):
    L, R = map(int, input().split())
    intervals.append((L, R))

intervals.sort()

merged = []
curL, curR = intervals[0]

for L, R in intervals[1:]:
    if L <= curR:  # 구간 겹치거나 붙는 경우
        if R > curR:
            curR = R
    else:  # 구간 떨어진 경우
        merged.append((curL, curR))
        curL, curR = L, R
merged.append((curL, curR))

# 병합된 구간 개수 = 파괴된 벽 덩어리 개수
# N - (파괴된 구간 길이)
destroyed = 0
for L, R in merged:
    destroyed += (R - L)

print(N - destroyed)
