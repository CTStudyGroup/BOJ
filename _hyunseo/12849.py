
'''
dp[1] = 2 1분이 주어졌을 때 2개의 경로
dp[2] = 5 
dp[3] = '''
board={}
board[0] = [1,2]
board[1] = [0,2,3]
board[2] = [0,1,3,4]
board[3] = [1,2,4,5]
board[4] = [2,3,5,7]
board[5]=[3,4,6]
board[6] = [5,7]
board[7]=[4,6]

n = int(input())
'''dp[시간][건물] = 경로의 수'''
dp = [[0]*8 for _ in range(n+1)]
dp[0][0] = 1
for time in range(n) :
    for node in range(0,8) :
        for neighbor in board[node] :
            dp[time+1][neighbor] = (dp[time+1][neighbor] + dp[time][node]) % 1000000007

print(dp[n][0])
