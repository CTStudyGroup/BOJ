import sys
input = sys.stdin.readline

# 1의 속력으로 이동
# 멈춰서 기다릴 수 있음
# T[i] 시각 이후에 그 위치를 지나면 i번 물건 회수 가능

N = int(input())
X = list(map(int, input().split()))
T = list(map(int, input().split()))

# 그리디
# 갈 땐 기다리지 말고 그 시점에 물건 있는 애들만 회수
# 올 땐 뒤에서부터 남은 물건 모두 회수할거고 기다려야하면 모두 기다림
# 오면서 한번에 싹 가져오면 됨 갔다 왔다 할필요 없음

T_arr = [-1] * (X[-1] + 1)
for i in range(N):
    T_arr[X[i]] = T[i]

end = X[-1]
time = 1
curr = 1
# 0 -> end까지
while curr < end:
    if 0 <= T_arr[curr] < time:  # 현재 위치에 물건이 있으면서, 회수 가능함
        T_arr[curr] = -1
    curr += 1
    time += 1

# end -> 0까지
while curr > 0:
    if 0 <= T_arr[curr]:  # 현재 위치에 물건 있으면
        if T_arr[curr] > time:  # 물건 나오기 기다려야 하면
            time += T_arr[curr] - time  # 회수할 때까지 기다림
        T_arr[curr] = -1
    curr -= 1
    time += 1

print(time)
