n = int(input())
distances = [int(input()) for _ in range(n)]

# 전체 합
total_sum = sum(distances)
target = total_sum / 2

# 원형을 풀기 위해 배열 2배로 늘리기
extended = distances * 2

# 누적합 (prefix sum)
prefix = [0]
for d in extended:
    prefix.append(prefix[-1] + d)

max_smaller = 0
end = 0

# 시작점을 하나씩 옮기며 탐색
for start in range(n):
    # end는 start로부터 최대 n까지만 갈 수 있음
    while end < start + n and prefix[end + 1] - prefix[start] <= target:
        end += 1
    
    # 후보 2개: end까지 구간합, end+1까지 구간합
    for e in [end, end + 1]:
        if e <= start + n:
            part_sum = prefix[e] - prefix[start]
            other_sum = total_sum - part_sum
            smaller = min(part_sum, other_sum)
            max_smaller = max(max_smaller, smaller)

print(max_smaller)