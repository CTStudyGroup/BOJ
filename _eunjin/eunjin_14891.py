from collections import deque

wheel1 = list(map(int, input()))
wheel2 = list(map(int, input()))
wheel3 = list(map(int, input()))
wheel4 = list(map(int, input()))
K = int(input())
command = [list(map(int, input().split())) for _ in range(K)]

wh1 = deque(wheel1[6:]+wheel1[:6])
wh2 = deque(wheel2[6:]+wheel2[:6])
wh3 = deque(wheel3[6:]+wheel3[:6])
wh4 = deque(wheel4[6:]+wheel4[:6])

# 0번째: 왼쪽 끝, 4번째: 오른쪽 끝
# wh1.append(wh1.popleft())  # 반시계 회전
# wh1.appendleft(wh1.pop())  # 시계 회전


for k in range(K):
    w, cmd = command[k]
    turn_arr = [0, 0, 0, 0]
    turn_arr[w-1] = cmd
    if w == 1:
        if wh2[0] != wh1[4]:
            turn_arr[1] = -turn_arr[0]
        if wh3[0] != wh2[4]:
            turn_arr[2] = -turn_arr[1]
        if wh4[0] != wh3[4]:
            turn_arr[3] = -turn_arr[2]
    elif w == 2:
        if wh1[4] != wh2[0]:
            turn_arr[0] = -turn_arr[1]
        if wh3[0] != wh2[4]:
            turn_arr[2] = -turn_arr[1]
        if wh4[0] != wh3[4]:
            turn_arr[3] = -turn_arr[2]
    elif w == 3:
        if wh4[0] != wh3[4]:
            turn_arr[3] = -turn_arr[2]
        if wh2[4] != wh3[0]:
            turn_arr[1] = -turn_arr[2]
        if wh1[4] != wh2[0]:
            turn_arr[0] = -turn_arr[1]
    else:
        if wh3[4] != wh4[0]:
            turn_arr[2] = -turn_arr[3]
        if wh2[4] != wh3[0]:
            turn_arr[1] = -turn_arr[2]
        if wh1[4] != wh2[0]:
            turn_arr[0] = -turn_arr[1]

    # 1번 톱니 회전
    if turn_arr[0] == 1:
        wh1.appendleft(wh1.pop())
    elif turn_arr[0] == -1:
        wh1.append(wh1.popleft())

    # 2번 톱니 회전
    if turn_arr[1] == 1:
        wh2.appendleft(wh2.pop())
    elif turn_arr[1] == -1:
        wh2.append(wh2.popleft())

    # 3번 톱니 회전
    if turn_arr[2] == 1:
        wh3.appendleft(wh3.pop())
    elif turn_arr[2] == -1:
        wh3.append(wh3.popleft())

    # 4번 톱니 회전
    if turn_arr[3] == 1:
        wh4.appendleft(wh4.pop())
    elif turn_arr[3] == -1:
        wh4.append(wh4.popleft())

answer = 0
if wh1[2]:
    answer += 1
if wh2[2]:
    answer += 2
if wh3[2]:
    answer += 4
if wh4[2]:
    answer += 8

print(answer)
