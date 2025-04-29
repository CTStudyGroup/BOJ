import sys
input = sys.stdin.readline
N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]

if N == 0:
    print(0)
    exit()

# dp
# 가장 위 색종이 길이를 기반으로 현재 색종이 추가
# # dp[x]: x번째 색종이까지 고려했을 때 쌓을 수 있는 최대 색종이 수

# paper.sort(key=lambda x: [-x[0], -x[1]])  # 크기가 가장 큰 것부터 정렬
# # print(paper)

# dp = [0] * N
# dp[0] = 1
# for i in range(1, N):
#     curr_y, curr_x = paper[i][0], paper[i][1]
#     for j in range(i - 1, -1, -1):
#         temp_y, temp_x = paper[j][0], paper[j][1]
#         if curr_y <= temp_y and curr_x <= temp_x:
#             dp[i] = max(dp[i], dp[j] + 1)
#         elif curr_x <= temp_y and curr_y <= temp_x:
#             paper[i][0] = curr_x
#             paper[i][1] = curr_y
#             dp[i] = max(dp[i], dp[j] + 1)

# # print(dp)
# print(max(dp))


# dp[x][y]: (y,x) 쌓을 수 있는 최대 색종이 수

paper.sort(key=lambda x: [-x[0], -x[1]])  # 크기가 가장 큰 것부터 정렬
print(paper)
R, C = 0, 0
for y, x in paper:
    R = max(R, y)
    C = max(C, x)

dp = [[0] * (C + 1) for _ in range(R + 1)]

for y, x in paper:
    dp[y][x] = 1

for i in range(N):
    curr_y, curr_x = paper[i][0], paper[i][1]
    dp[curr_y][curr_x] = 1
    for j in range(i - 1, -1, -1):
        temp_y, temp_x = paper[j][0], paper[j][1]
        if curr_y <= temp_y and curr_x <= temp_x:
            dp[curr_y][curr_x] = max(dp[curr_y][curr_x], dp[temp_y][temp_x] + 1)
        if curr_x <= temp_y and curr_y <= temp_x:
            dp[curr_x][curr_y] = max(dp[curr_x][curr_y], dp[temp_y][temp_x] + 1)

for row in dp:
    for elem in row:
        print(elem, end=" ")
    print()

answer = 0
for row in dp:
    answer = max(answer, max(row))

print(answer)


# # dp[x][i]: x번째 색종이까지 고려했을 때(i=0:뒤집지 않음, i=1:뒤집음) 쌓을 수 있는 최대 색종이 수

# paper.sort(key=lambda x: [-x[0], -x[1]])  # 크기가 가장 큰 것부터 정렬
# # print(paper)

# dp = [[0, 0] for _ in range(N)]
# dp[0][0] = 1
# dp[0][1] = 1
# for i in range(1, N):
#     curr_y, curr_x = paper[i][0], paper[i][1]
#     dp[i][0], dp[i][1] = 1, 1
#     for j in range(i - 1, -1, -1):
#         temp_y, temp_x = paper[j][0], paper[j][1]
#         if curr_y <= temp_y and curr_x <= temp_x:
#             dp[i][0] = max(dp[i][0], dp[j][0] + 1)
#         elif curr_x <= temp_y and curr_y <= temp_x:
#             dp[i][1] = max(dp[i][1], dp[j][0] + 1, dp[j][1] + 1)

# # print(dp)
# print(max(dp[N - 1]))
