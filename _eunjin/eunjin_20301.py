N, K, M = map(int, input().split())

queue = list(i for i in range(1, N+1))

idx = K-1
direction = False
pop_num = 0

# 1 2 3 4 5 6 7
# 1 2 3 4 5 6, idx:6
# 1 2 3 4 5, idx:5
# 1 2 3 5, idx:3


while True:
    print(queue.pop(idx))
    if not queue:  # 모든 사람을 제거한 경우
        break

    pop_num += 1

    if pop_num == M:
        direction = not direction
        pop_num = 0

    if direction:  # 왼쪽 방향
        temp_idx = idx-K
        if temp_idx < 0:
            temp_idx = temp_idx % len(queue)
        idx = temp_idx
    else:  # 오른쪽 방향
        temp_idx = idx+K-1
        if temp_idx >= len(queue):
            temp_idx = temp_idx % len(queue)
        idx = temp_idx

    # print(queue, ", next idx:", idx, ", dir:", direction)
