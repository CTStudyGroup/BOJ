N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

# 중복 허용 순열

def backtracking():
    if len(arr) == M:
        print(*arr)
        return

    for i in range(N):
        arr.append(nums[i])
        backtracking()
        arr.pop()

arr = []
backtracking()
