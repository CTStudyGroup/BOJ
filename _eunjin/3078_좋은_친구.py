import sys
input = sys.stdin.readline

N, K = map(int, input().split())
length = []
for i in range(N):
    st = input().strip()
    length.append(len(st))

# 등수의 차이가 K보다 작거나 같으면서 이름의 길이가 같은 친구
# 누적합? 슬라이딩 윈도우?

dp = [0] * (21)  # dp[L]: 길이가 L인 학생의 수

dp[length[0]] = 1  # 첫번쨰 학생의 길이
answer = 0
for n in range(1, N):
    if n - K - 1 >= 0:
        l = length[n - K - 1]
        dp[l] -= 1

    l = length[n]
    # print(answer, "+", dp[l], "= ", answer + dp[l])
    answer += dp[l]
    dp[l] += 1

# print(dp)
print(answer)

