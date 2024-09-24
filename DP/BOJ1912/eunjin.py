# 입력 받기
N = int(input())
input_arr = list(map(int, input().split()))

# n이 100,000까지 가능하므로 브루트포스 불가
# 앞에서부터 합이 최대가 되도록 정수 선택한다고해도 뒤에서 더 큰 최대 합을 갖는 구간이 생길 수 있으므로 그리디 불가

arr = [0]
for i in range(N):
    arr.append(input_arr[i])

# dp[x]: x를 포함하는, x까지의 최대 연속 합
# x번째 정수까지의 최대 연속 합은 x-1번째 정수까지의 최대 연속합에 x 자신까지 더한 값과, x 자신 중 최댓값이다
# dp[x-1]+x 가 더 크면 x-1번째 정수까지 고르고 x도 고르면 되고, 그냥 x가 더 크면 x-1번째까지의 연속 합을 포기하고 x 자신만 선택하면 된다
dp = [0] * (N+1)
if(N == 1):
    print(arr[1])
else:
    dp[0] = min(input_arr)
    dp[1] = arr[1]
    for x in range(2, N+1):
        dp[x] = max(dp[x-1]+arr[x], arr[x])
    # print(dp)
    print(max(dp))
