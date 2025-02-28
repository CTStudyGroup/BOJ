N = int(input())
ingredients = [list(map(int, input().split())) for _ in range(N)]

mn = float('inf')

def backtracking(idx, sour, bitter, used):
    global mn

    if used > 0:
        mn = min(mn, abs(bitter - sour))

    if idx == N:
        return

    s, b = ingredients[idx]

    # 해당 재료 사용하는 경우
    backtracking(idx + 1, sour * s, bitter + b, used + 1)

    # 해당 재료 사용 안하는 경우
    backtracking(idx + 1, sour, bitter, used)

backtracking(0, 1, 0, 0)

print(mn)
