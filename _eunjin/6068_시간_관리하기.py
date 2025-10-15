import sys
input = sys.stdin.readline

N = int(input())
task = [list(map(int, input().split())) for _ in range(N)]

# 그리디
# 각 일마다 최대한 늦게 시작하기
task.sort(key=lambda x: -x[1])  # 마감 시간이 늦은 순으로 정렬
used = [False] * (10**6 + 1)

for time, deadline in task:
    if time > deadline:
        print(-1)
        exit()

    assigned = False
    for i in range(deadline - 1, -1, -1):
        if not used[i]:
            for j in range(time):
                used[i - j] = True
            assigned = True
            break

    if not assigned:  # 해당 task를 끝낼 수 없음
        print(-1)
        exit()

for i in range(len(used)):  # 가장 처음으로 일을 시작하는 시간 출력
    if used[i]:
        print(i)
        exit()
