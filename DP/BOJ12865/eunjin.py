# 입력 받기
N, K = map(int, input().split())
W = [0]
V = [0]
for _ in range(N):
    w, v = map(int, input().split())
    W.append(w)
    V.append(v)

# 브루트포스: 연산 횟수가 2^100이므로 시간초과, 사용 불가
# 그리디: 매번 가치가 가장 큰 물품을 고른다고 해서 그게 최적의 해가 되는 것은 아니므로 사용 불가
# dp로 풀어야 한다

# dp[k][x]: 가능한 최대 무게가 k일 때 x번째 물품까지의 가치합 최댓값
dp = [[0]*(N+1) for _ in range(K+1)]
for k in range(1, K+1):
    for x in range(1, N+1):
        if(k < W[x]):  # x번째 물품 추가 못하는 경우
            dp[k][x] = dp[k][x-1]
        else:  # x번째 물품 추가 가능한 경우
            # x번째 물품 추가 O, 추가 X 중에서 더 큰 값을 선택
            dp[k][x] = max(dp[k-W[x]][x-1]+V[x], dp[k][x-1])


# for row in dp:
#     for col in row:
#         print(col, end=" ")
#     print()
print(dp[K][N])
