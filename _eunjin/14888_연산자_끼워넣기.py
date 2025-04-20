import sys
N = int(input())
A = list(map(int, input().split()))
count = list(map(int, input().split()))  # +, -, x, /

total = []  # 전체 연산자 조합

def backtracking():
    if len(arr) == N - 1:
        total.append(tuple(arr))
        return

    for i in range(4):
        if count[i]:  # 해당 부호 선택할 수 있으면
            count[i] -= 1
            arr.append(i)
            backtracking()
            arr.pop()
            count[i] += 1

arr = []
backtracking()

mx = -sys.maxsize
mn = sys.maxsize

for calc in total:
    result = A[0]
    for i in range(N - 1):
        if calc[i] == 0:
            result += A[i + 1]
        elif calc[i] == 1:
            result -= A[i + 1]
        elif calc[i] == 2:
            result *= A[i + 1]
        else:
            if result < 0:
                result = -((-result) // A[i + 1])
            else:
                result = result // A[i + 1]
    mx = max(mx, result)
    mn = min(mn, result)

print(mx)
print(mn)

