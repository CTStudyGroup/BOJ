# 입력 받기
N = int(input())

house = [list(map(int, input().split())) for _ in range(N)]

# 빨강, 초록, 파랑 list
# 각 자리에는 i번째 집을 해당 색상으로 칠할 때, 0~i번째 집까지의 비용의 최솟값을 저장
red = [-1]*N
green = [-1]*N
blue = [-1]*N

red[0] = house[0][0]
green[0] = house[0][1]
blue[0] = house[0][2]

for i in range(1, N):
    #print("red[", i, "] =", min(green[i-1], blue[i-1]), " +", house[i][0])
    red[i] = min(green[i-1], blue[i-1])+house[i][0]

    #print("green[", i, "] =", min(red[i-1], blue[i-1]), " +", house[i][1])
    green[i] = min(red[i-1], blue[i-1])+house[i][1]

    #print("blue[", i, "] =", min(red[i-1], green[i-1]), " +", house[i][2])
    blue[i] = min(red[i-1], green[i-1])+house[i][2]


# print("======")
# print(red)
# print(green)
# print(blue)

print(min(red[N-1], green[N-1], blue[N-1]))
