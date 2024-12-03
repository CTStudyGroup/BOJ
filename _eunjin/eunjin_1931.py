import sys
input = sys.stdin.readline

# 입력 받기
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

# print(arr)

sorted_arr = sorted(arr, key=lambda x: (x[1], x[0]))
# print(sorted_arr)

result = 0
endTime = 0

for time in sorted_arr:
    if time[0] >= endTime:
        endTime = time[1]
        result += 1

print(result)
