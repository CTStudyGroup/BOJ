N, L, R, X = map(int, input().split())
arr = list(map(int, input().split()))

# N개 문제에 대해 각각 고르는 경우/고르지 않는 경우 탐색 = 총 2^N개 경우의 수
# 백트래킹

def backtracking(i):
    global answer
    if i == N:  # N개 문제에 대한 모든 경우의 수 탐색
        if len(picked) < 2:  # 두 문제 이상 선택해야 함
            return

        # 문제 난이도의 합은 L이상 R이하
        sm = 0
        lowest = int(10e9)
        highest = 0
        for p in picked:
            sm += arr[p]
            lowest = min(lowest, arr[p])
            highest = max(highest, arr[p])

        if sm < L or sm > R:
            return

        # 가장 어려운 문제와 쉬운 문제의 난이도 차이는 X이상
        if highest - lowest < X:
            return

        answer += 1
        return

    # i번째 문제 고르는 경우
    picked.append(i)
    backtracking(i + 1)
    picked.pop()

    # i번째 문제 고르지 않는 경우
    backtracking(i + 1)

answer = 0
picked = []
backtracking(0)
print(answer)
