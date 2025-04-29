import sys
input = sys.stdin.readline

N, K = map(int, input().split())
belt = list(map(int, input().split()))

# 1. 벨트와 로봇 한 칸 회전
# 2. 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한칸 이동, 이동 불가하면 이동X
#    1. 로봇이 이동하려면 이동하려는 칸에 로봇이 없어야 하고, 내구도가 1 이상 남아있어야 함
# 3. 올리는 위치에 있는 칸의 내구도가 0이 아니면 로봇 추가
# 4. 내구도가 0인 칸의 개수가 K개 이상이면 과정 종료

robots = [False] * 2 * N  # 로봇의 위치 저장
up_p = 0
down_p = N - 1

def rotate():
    global up_p, down_p
    up_p = (up_p - 1) % (2 * N)
    down_p = (down_p - 1) % (2 * N)
    if robots[down_p]:
        robots[down_p] = False

def move_robots():
    rp = down_p  # 내리는 위치 한칸 전부터 탐색 시작

    for _ in range(N):
        rp = (rp - 1) % (2 * N)
        nxt = (rp + 1) % (2 * N)
        if robots[rp]:
            if belt[nxt] < 1 or robots[nxt]:
                continue
            if nxt == down_p:
                robots[rp] = False
                belt[nxt] -= 1
            else:
                robots[rp] = False
                robots[nxt] = True
                belt[nxt] -= 1

def add_robot():
    if belt[up_p]:
        belt[up_p] -= 1
        robots[up_p] = True

def check_end():
    cnt = 0
    for b in belt:
        if b == 0:
            cnt += 1

    return cnt < K

answer = 0
while(check_end()):
    rotate()
    move_robots()
    add_robot()
    answer += 1

print(answer)

