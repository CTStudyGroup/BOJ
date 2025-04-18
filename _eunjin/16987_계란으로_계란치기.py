import sys
sys.setrecursionlimit(1e6)

N = int(input())
S = []
W = []
for _ in range(N):
    s, w = map(int, input().split())
    S.append(s)
    W.append(w)

# 계란으로 상대 계란을 치면, 각 계란의 내구도는 상대 계란의 무게만큼 깎인다.

# 0번째 계란에서 시작해서 N-1번째 계란까지 잡기
# 잡은게 N-1번째 계란(제일 오른쪽 계란)이면 전체 과정 종료
# 한 계란으로 하나의 상대 계란만 칠 수 있다.


# n번째 계란 잡고 진행
def backtracking(n):
    global answer
    if n == N:
        broken = sum(1 for s in S if s <= 0)
        answer = max(answer, broken)
        return

    if S[n] <= 0:
        backtracking(n + 1)
        return

    is_hit = False
    for i in range(N):
        if i == n or S[i] <= 0:
            continue

        S[i] -= W[n]
        S[n] -= W[i]
        is_hit = True

        backtracking(n + 1)

        S[i] += W[n]
        S[n] += W[i]

    if not is_hit:
        backtracking(n + 1)

answer = 0
backtracking(0)
print(answer)
