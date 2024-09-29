# 입력 받기
N = int(input())

# 가로 길이가 1, 2인 사각형 둘 중에 선택해서 배치하면 된다.
# 1,2의 합으로 N을 나타내는 것과 같다
if(N == 1):
    print(1)
else:

    dp = [0]*(N+1)
    dp[1] = 1
    dp[2] = 2

    for i in range(3, N+1):
        dp[i] = dp[i-1]+dp[i-2]

    print(dp[N] % 10007)
