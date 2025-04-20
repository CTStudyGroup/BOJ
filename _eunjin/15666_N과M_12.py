N, M = map(int, input().split())
nums = list(map(int, input().split()))

nums.sort()

# 같은 거 여러번 고르기 가능
# 비내림차순

def backtracking(n):
    if len(arr) == M:
        print(*arr)
        return

    prev = -1
    for i in range(n, N):
        if nums[i] != prev:
            arr.append(nums[i])
            prev = nums[i]
            backtracking(i)
            arr.pop()

arr = []
backtracking(0)
