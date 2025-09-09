import sys
input = sys.stdin.readline

N = int(input())
arr = [tuple(map(int, input().split())) for _ in range(N)]

# (소요시간, 마감시간)
arr.sort(key=lambda x: x[1])  # deadline 기준 정렬

total = 0
ans = sys.maxsize

for t, d in arr:
    total += t
    ans = min(ans, d - total)  # d - 지금까지 걸린 시간 = 최대 기상 가능 시간

print(ans if ans >= 0 else -1)
