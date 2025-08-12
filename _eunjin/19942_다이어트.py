import sys
input = sys.stdin.readline

N = int(input())
mp, mf, ms, mv = map(int, input().split())
ingredients = []
for _ in range(N):
    ingredients.append(list(map(int, input().split())))

# 완전탐색 백트래킹?

# 현재 재료 조합이 조건을 만족하는지 여부 반환
def valid(arr):
    tmp, tmf, tms, tmv = 0, 0, 0, 0
    for i in arr:
        tmp += ingredients[i][0]
        tmf += ingredients[i][1]
        tms += ingredients[i][2]
        tmv += ingredients[i][3]

    if tmp >= mp and tmf >= mf and tms >= ms and tmv >= mv:
        return True
    return False

def backtracking(n, price):
    global mx_price, answer

    if price < mx_price and valid(arr):
        answer = arr[:]
        mx_price = price

    if n == N:
        return

    # n번째 재료 고르는 경우
    arr.append(n)
    backtracking(n + 1, price + ingredients[n][4])
    arr.pop()

    # n번째 재료 고르지 않는 경우
    backtracking(n + 1, price)

# mx_price 초기화
mx_price = 1
for i in range(N):
    mx_price += ingredients[i][4]

# backtracking 실행
answer = []
arr = []
backtracking(0, 0)

if answer:
    print(mx_price)
    for i in range(len(answer)):
        answer[i] += 1
    print(*answer)
else:
    print(-1)
