import sys
N = int(input())
A = list(map(int, input().split()))
calc = list(map(int, input().split()))  # +,-,*,/

def calculate(n, depth, c):  # 기존 수, 다음 수 인덱스, 연산자 인덱스
    if c == 0:
        return n + A[depth]
    if c == 1:
        return n - A[depth]
    if c == 2:
        return n * A[depth]
    if c == 3:
        if n < 0 and A[depth] > 0:
            return (n * (-1) // A[depth]) * (-1)
        else:
            return n // A[depth]

# 백트래킹으로 모든 경우 탐색
def backtracking(n, depth):
    global mx_answer, mn_answer
    if depth == N:
        mx_answer = max(mx_answer, n)
        mn_answer = min(mn_answer, n)
        return

    for i in range(4):
        if calc[i]:  # 해당 연산자 사용 가능하면
            calc[i] -= 1
            backtracking(calculate(n, depth, i), depth + 1)
            calc[i] += 1

mx_answer = (-1) * sys.maxsize
mn_answer = sys.maxsize

backtracking(A[0], 1)

print(mx_answer)
print(mn_answer)
