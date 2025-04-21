from collections import deque
import sys
input = sys.stdin.readline
T = int(input())

clock = []
for _ in range(T):
    inp = list(input())  # 10101111
    clock.append(deque([inp[6], inp[7], inp[0], inp[1], inp[2], inp[3], inp[4], inp[5]]))

K = int(input())
cmd_list = [list(map(int, input().split())) for _ in range(K)]

# 인접한 톱니의 극이 다르면 서로 다른 방향으로 회전
# 인접한 톱니의 극이 같으면 회전 X

# 회전해야할 시계의 범위 구하기
def get_rotates(n):
    ret = []
    # N번 시계 기준 왼쪽 시계들 탐색
    for i in range(n - 1, -1, -1):
        if clock[i + 1][0] != clock[i][4]:
            ret.append(i)
        else:
            break

    # N번 시계 기준 오른쪽 시계들 탐색
    for i in range(n + 1, T):
        if clock[i][0] != clock[i - 1][4]:
            ret.append(i)
        else:
            break

    return ret

# 시계 회전
# n번 시계를 dirr 방향으로 회전
# 나머지 arr의 시계를 회전
def rotate(arr, n, dirr):
    clock[n].rotate(dirr)

    for idx in arr:
        if abs(idx - n) % 2 == 1:
            clock[idx].rotate(-dirr)
        else:
            clock[idx].rotate(dirr)

for cl, dirr in cmd_list:
    arr = get_rotates(cl - 1)
    rotate(arr, cl - 1, dirr)

answer = 0
for cl in clock:
    if cl[2] == "1":
        answer += 1

print(answer)
