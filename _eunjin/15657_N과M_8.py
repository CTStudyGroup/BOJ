N, M = map(int, input().split())
nums = list(map(int, input().split()))

# 중복 가능
# 비내림차순

nums.sort()

def backtracking(n):
    if len(arr) == M:
        print(*arr)
        return

    for i in range(n, N):
        arr.append(nums[i])
        backtracking(i)
        arr.pop()

arr = []
backtracking(0)
