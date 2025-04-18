# N번 진행
# 한 이닝에 3아웃이면 해당 이닝 종료, 공격 수비 전환
# 3아웃 나올 때까지 1~9번 타자 반복, 이전 이닝의 순서를 다음 이닝에서도 유지
# 1->2->3->홈 으로 오면 점수 +1
# 이닝 시작할 때 주자 초기화

from itertools import permutations

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]

# n번 타자 공 치기
def hit_ball(n):
    global score, g1, g2, g3
    before = score
    if type[n] == 1:
        score += g3
        g3 = g2
        g2 = g1
        g1 = 1
    elif type[n] == 2:
        score += g2 + g3
        g3 = g1
        g2 = 1
        g1 = 0
    elif type[n] == 3:
        score += g1 + g2 + g3
        g3 = 1
        g2, g1 = 0, 0
    elif type[n] == 4:
        score += g1 + g2 + g3 + 1
        g1, g2, g3 = 0, 0, 0
    else:  # 아웃
        return True
    return False

answer = 0
for perm in permutations(range(1, 9), 8):  # 1번 선수는 4번 타자로 지정하고 나머지 선수 순서 조합 결정
    players = list(perm[:3]) + [0] + list(perm[3:])
    idx = 0  # 시작 player 리스트의 idx
    score = 0
    for t in range(N):  # 각 이닝 마다
        outcnt = 0
        type = matrix[t]
        g1, g2, g3 = 0, 0, 0  # 1루,2루,3루
        while outcnt < 3:  # 3아웃까지
            out = hit_ball(players[idx])
            if out:
                outcnt += 1
            idx = (idx + 1) % 9  # 다음 타자로 커서 이동

    answer = max(answer, score)

print(answer)
