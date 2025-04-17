T = int(input())

def get_dist(arr):
    ret = 0
    for i in range(4):
        if mbti[arr[0]][i] != mbti[arr[1]][i]:
            ret += 1
        if mbti[arr[1]][i] != mbti[arr[2]][i]:
            ret += 1
        if mbti[arr[0]][i] != mbti[arr[2]][i]:
            ret += 1
    return ret

def dfs(n, depth, arr):
    global answer
    if depth == 3:
        answer = min(answer, get_dist(arr))
        return

    for i in range(n, N):
        arr.append(i)
        dfs(i + 1, depth + 1, arr)
        arr.pop()


for _ in range(T):
    N = int(input())
    mbti = list(input().split())
    if N > 32:
        print(0)
    else:
        answer = 1e9
        dfs(0, 0, [])
        print(answer)
