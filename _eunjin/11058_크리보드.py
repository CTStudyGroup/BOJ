N = int(input())

# dp
# dp[x]: 버튼 x번 눌렀을 때 최대 A의 개수
dp = [0] * (N + 1)
if N <= 5:
    print(N)
    exit()

dp[3] = 3
dp[4] = 4
dp[5] = 5

buffer = [0] * (N + 1)

for x in range(6, N + 1):
    # v1 = dp[n - 1] + 1  # 그냥 A 하나 더 출력
    v1 = dp[x - 1] + buffer[x - 1]  # 기존에 갖고있던 버퍼 ctrl V
    v2, mx_buff = 0, 0

    for i in range(3, x + 1):
        if dp[x - i] * (i - 1) > v2:
            v2 = dp[x - i] * (i - 1)
            mx_buff = dp[x - i]
        elif dp[x - i] * (i - 1) == v2:
            mx_buff = max(mx_buff, mx_buff)

    if v1 == v2:
        if mx_buff > buffer[x - 1]:
            dp[x] = v2
            buffer[x] = mx_buff
        else:
            dp[x] = v1
            buffer[x] = buffer[x - 1]
    elif v1 > v2:
        dp[x] = v1
        buffer[x] = buffer[x - 1]
    else:
        dp[x] = v2
        buffer[x] = mx_buff

print(dp[N])
