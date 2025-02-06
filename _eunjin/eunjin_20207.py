N = int(input())

tasks = [list(map(int, input().split())) for _ in range(N)]

tasks = sorted(tasks, key=lambda x: (x[0], -x[1]))
# print(tasks)

start_dates = []
end_dates = []
size = 0


def is_continuous(start):
    if end_dates and start > max(end_dates)+1:
        return False
    return True


def get_end_idx(start):
    for i in range(len(end_dates)):
        if end_dates[i] < start:
            return i

    return -1


for i in range(N):
    start, end = tasks[i]
    # print("start:", start, ", end:", end)
    if is_continuous(start):  # 해당 일정이 연속된 일정인 경우
        end_idx = get_end_idx(start)
        if end_idx == -1:  # 구간 하나 추가
            start_dates.append(start)
            end_dates.append(end)
        else:  # 이미 존재하는 구간에 일정 추가
            end_dates[end_idx] = end
        # print("continuous, start_dates:", start_dates, ", end_dates:", end_dates)
    else:  # 해당 일정이 연속된 일정이 아닌 경우
        size += (max(end_dates)-min(start_dates)+1)*len(start_dates)
        start_dates = [start]
        end_dates = [end]
        # print("not continuous, size:", size)

if start_dates and end_dates:
    size += (max(end_dates)-min(start_dates)+1)*len(start_dates)

print(size)
