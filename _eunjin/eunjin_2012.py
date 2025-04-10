import sys
input = sys.stdin.readline

N = int(input())
arr = [int(input()) for _ in range(N)]

# 그리디?
arr.sort()
answer = 0
for i in range(N):
    answer += abs(arr[i] - i - 1)
    # print("answer:", answer)

print(answer)
