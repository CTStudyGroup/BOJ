# 입력 받기
N = int(input())
arr = [0]
for _ in range(N):
    arr.append(int(input()))

dp = [[-1 for _ in range(N+1)]for _ in range(N+1)]

# 대각선을 0으로 초기화
for i in range(N+1):
    dp[i][i] = 0

# dp[x][y]: x에서 출발해 y까지 계단을 밟았을 때의 점수 최댓값

for y in range(1, N+1):
    for x in range(y-1, -1, -1):
        if(y == x+1):
            dp[x][y] = arr[y]
        elif(y == x+2):
            dp[x][y] = arr[y-1]+arr[y]
        else:
            dp[x][y] = max(dp[x][y-2]+arr[y], dp[x][y-3]+arr[y-1]+arr[y])


# for row in dp:
#     for elem in row:
#         print(elem, end=" ")
#     print()

print(dp[0][N])
