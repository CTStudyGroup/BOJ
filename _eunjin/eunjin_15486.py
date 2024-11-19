import sys
input = sys.stdin.readline

# 입력 받기
N = int(input())
t = [0]
p = [0]

for _ in range(N):
    T, P = map(int, input().split())
    t.append(T)
    p.append(P)

# dp list 초기화
dp = [0 for _ in range(N+1)]

for i in range(1, N+1):
    dp[i] = max(dp[i], dp[i-1])  # 일단 현재 날짜를 최댓값으로 초기화
    date = i+t[i]-1  # 일이 끝나는 날
    if date <= N:
        # date 날짜의 값은 현재 일을 하지 않는 경우와 하는 경우 중의 최댓값
        dp[date] = max(dp[date], dp[i-1]+p[i])
    # print("i:", i, dp)

# print(dp)
print(max(dp))
