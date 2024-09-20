# 입력 받기
N = int(input())
A = list(map(int, input().split()))

# dp[i]
# 0~i번째 원소 중, i번째 원소를 포함하는 가장 긴 증가하는 부분 수열 길이
dp = [1]*N

for i in range(1, N):
    low_idxs = []     # low_idxs: i번째 원소보다 작은 원소들의 인덱스 list
    for x in range(i-1, -1, -1):
        # print("i:", i, ", x:", x)
        if(A[i] > A[x]):
            low_idxs.append(x)

    #print("low_idx:", low_idxs)

    if(low_idxs):
        max_dp_idx = low_idxs[0]
        for idx in low_idxs:
            if(dp[idx] > dp[max_dp_idx]):
                max_dp_idx = idx
        # print("i:", i, ", max_dp_idx:", max_dp_idx)

        dp[i] = dp[max_dp_idx]+1
    # print("dp:", dp)

# print(dp)
print(max(dp))


# for i in range(1, N):
#     for x in range(i):
#         if(A[i] > A[x]):
#             dp[i] = max(dp[i], dp[x]+1)

# print(max(dp))
