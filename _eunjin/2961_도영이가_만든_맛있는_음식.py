N = int(input())
taste = [list(map(int, input().split())) for _ in range(N)]

# 백트래킹 2^N

def backtracking(i):
    global answer
    if i == N:
        if len(arr) > 0:
            sour, bitter = 1, 0
            for k in arr:
                sour *= taste[k][0]
                bitter += taste[k][1]
            answer = min(answer, abs(sour - bitter))
        return

    # i번째 재료 선택 하는 경우
    arr.append(i)
    backtracking(i + 1)
    arr.pop()

    # i번째 재료 선택 안하는 경우
    backtracking(i + 1)

arr = []
answer = 1e10
backtracking(0)
print(answer)
