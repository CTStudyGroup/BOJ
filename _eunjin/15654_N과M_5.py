N, M = map(int, input().split())
nums = list(map(int, input().split()))

nums.sort()

# 중복X 순열

def backtracking():
    if len(arr) == M:
        print(*arr)
        return()

    for i in range(N):
        if not visited[i]:
            arr.append(nums[i])
            visited[i] = True
            backtracking()
            arr.pop()
            visited[i] = False

arr = []
visited = [False] * N
backtracking()
