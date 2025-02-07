from collections import deque
N = int(input())
tasks = [list(map(int, input().split())) for _ in range(N)]

tasks = deque(sorted(tasks, key=lambda x: (-x[1], -x[0])))

end_times = list(map(lambda x: x[1], tasks))

time = [0]*(max(end_times)+1)

# 가장 늦게 끝내도 되는 일 + 시간이 오래걸리는 일부터 배정 시작
while tasks:
    T, end = tasks.popleft()
    cnt = 0
    idx = -1
    for i in range(end, -1, -1):
        if time[i] == 0:
            cnt += 1
        else:
            cnt = 0
        if cnt == T:
            idx = i
            break
    if idx == -1:  # 해당 일 수행 불가
        print(-1)
        exit()
    else:  # 해당 일을 idx부터 시작하는 것으로 처리
        for i in range(idx, idx+T):
            time[i] = 1
        # print(time)

for i in range(len(time)):
    if time[i] == 1:
        print(i-1)
        exit()
