import sys
input = sys.stdin.readline

N = int(input())
board = [0]+list(map(int, input().split()))

# dp[x][y]: x부터 y까지가 팰린드롬인지 여부
# dp 초기화
dp = [[0]*(N+1) for _ in range(N+1)]

for i in range(1, N+1):
    dp[i][i] = 1
for i in range(1, N):
    if board[i] == board[i+1]:
        dp[i][i+1] = 1

# dp[x][y] = x번째, y번째 값이 같음 && x+1부터 y-1까지가 팰린드롬
for j in range(2, N):
    for i in range(N-j+1):
        k = j+i
        # print("dp[", i, "][", k, "] = dp[", i+1, "][", k-1, "]")
        if dp[i+1][k-1] and board[i] == board[k]:
            dp[i][k] = 1


# for x in dp:
#     for y in x:
#         print(y, end=" ")
#     print()

M = int(input())
for _ in range(M):
    s, e = map(int, input().split())
    print(dp[s][e])
