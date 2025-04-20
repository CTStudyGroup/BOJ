N, M = map(int, input().split())
nums = [0] + list(map(int, input().split()))

nums.sort()

# 오름차순 수열

def backtracking(n):
    if len(arr) == M:
        print(*arr)
        return

    for i in range(n + 1, N + 1):
        arr.append(nums[i])
        backtracking(i)
        arr.pop()

arr = []
backtracking(0)

