import bisect

N = int(input())
arr = list(map(int, input().split()))

LIS = []

for num in arr:
    idx = bisect.bisect_left(LIS, num)  # num이 들어갈 위치 (lower bound)
    if idx == len(LIS):
        LIS.append(num)  # num이 가장 크면 LIS 확장
    else:
        LIS[idx] = num   # 아니면 적절한 위치에 덮어쓰기 (더 작은 값 유지)

# print(LIS)
print(len(LIS))
