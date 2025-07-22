N = int(input())
checkpoints = []
for _ in range(N):
    checkpoints.append(list(map(int, input().split())))


if N == 3 :
    print(abs(checkpoints[0][0] - checkpoints[2][0]) + abs(checkpoints[0][1] - checkpoints[2][1]))
    exit()
# 0부터 idx까지의 거리 합
dp_from_0 = [0]*N
# N부터 idx까지의 거리 합
dp_from_N = [0]*N

# 거리 계산 (이거 sqrt로 계산하고 있었음)
def calculate_distance(arr1, arr2 ) :
    x1, y1 = arr1
    x2, y2 = arr2
    return abs(x1-x2) + abs(y1-y2)

# dp 미리 계산
from_0, from_N = 0,0
for i in range(1, N-1) :
    from_0 +=calculate_distance(checkpoints[i], checkpoints[i-1])
    from_N += calculate_distance(checkpoints[(N-1) - i], checkpoints[N-i])
    dp_from_0[i] = from_0
    dp_from_N[N - 1 - i ] = from_N

print(dp_from_0)
print(dp_from_N)
answer = float('inf')
# 후보군 순회하며 answer 갱신
for skip in range(1, N-1) :
    answer = min(answer, dp_from_0[skip-1] + dp_from_N[skip + 1]+ calculate_distance(checkpoints[skip-1], checkpoints[skip+1]))

print(answer)
