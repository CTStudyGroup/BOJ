import sys
input = sys.stdin.readline


def existLarger(value):
    global queue
    for elem in queue:
        if elem[1] > value:
            return True
    return False


# 입력 받기
T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    queue = list(enumerate(arr))
    result = []
    # print(queue)

    while queue:
        idx, value = queue[0]
        if existLarger(value):
            queue.append((idx, value))
        else:
            result.append((idx, value))

        queue.pop(0)
        # print("idx:", idx, "value:", value, ",queue:", queue)

    # print(result)

    for i in range(len(result)):
        if result[i][0] == M:
            print(i+1)
