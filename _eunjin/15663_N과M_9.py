N, M = map(int, input().split())
nums = list(map(int, input().split()))

# 입력에는 중복 있을 수 있고 출력은 중복 없어야 함
# 그전에 고른걸 또 다시 고를 수 없음
nums.sort()

answer = set()

def backtracking():
    if len(arr) == M:
        answer.add(tuple(arr))
        return

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

for ans in sorted(answer):
    print(' '.join(map(str, ans)))
