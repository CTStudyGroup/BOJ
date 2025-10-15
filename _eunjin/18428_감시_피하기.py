from itertools import combinations
import sys
input = sys.stdin.readline

N = int(input())
matrix = [list(input().strip().split()) for _ in range(N)]

# 빈칸,선생님 좌표 구하기
blanks = []
teachers = []
for y in range(N):
    for x in range(N):
        if matrix[y][x] == 'X':
            blanks.append((y, x))
        elif matrix[y][x] == "T":
            teachers.append((y, x))

# 해당 선생님 좌표에서 감시했을 때 학생 발견 여부
dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]
def search(sy, sx):
    for i in range(4):
        ny, nx = sy + dy[i], sx + dx[i]
        while (0 <= ny < N) and (0 <= nx < N):
            if matrix[ny][nx] == "S":
                return True
            elif matrix[ny][nx] == "X" or matrix[ny][nx] == "T":
                ny += dy[i]
                nx += dx[i]
            else:  # O
                break
    return False


 # N*N 좌표 중 장애물 설치할 좌표 3개 선택하는 모든 조합
for comb in combinations(blanks, 3):
    for by, bx in comb:
        matrix[by][bx] = 'O'

    flag = True
    for ty, tx in teachers:
        found = search(ty, tx)
        if found:
            flag = False

    if flag:
        print("YES")
        exit()

    for by, bx in comb:
        matrix[by][bx] = "X"

print("NO")



