import sys

input = sys.stdin.readline

N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

# score[y][x]: (y,x) 좌표에 남아있는 양분
score = [[5] * N for _ in range(N)]

# trees[y][x]: (y,x) 좌표에 존재하는 나무의 나이 list
trees = [[[] for _ in range(N)] for _ in range(N)]


dy = [-1, -1, -1, 0, 0, 1, 1, 1]
dx = [-1, 0, 1, -1, 1, -1, 0, 1]

for i in range(M):
    x, y, z = map(int, input().split())
    trees[x - 1][y - 1].append(z)

# 봄
# 나무가 자신의 나이만큼 양분 먹으면서 나이 +1
# 하나의 칸에 여러 나무가 있으면, 어린 나무부터 양분 먹음
# 자신의 나이만큼 먹을 수 없으면 즉시 죽음
def spring(agefive):
    # print("= spring =")
    # trees matrix 돌면서 나무 나이순 정렬 + 나이 먹기
    for y in range(N):
        for x in range(N):
            if not trees[y][x]:
                continue
            arr = sorted(trees[y][x])  # 나무 나이가 담긴 배열

            temp = []

            for age in arr:
                if age > score[y][x]:
                    dead.append((y, x, age))  # 죽는 나무에 추가

                else:
                    score[y][x] -= age  # 양분 먹음

                    if (age + 1) % 5 == 0:  # 나이 먹으면 5의 배수가 되는 경우
                        agefive.append((y, x))

                    temp.append(age + 1)  # 나이 +1

            trees[y][x] = temp  # 나이 먹고 남은 나무로 업데이트

# 여름
# 봄에 죽은 나무마다 나이//2 만큼 해당 칸에 양분으로 추가
def summer(dead):
    # print("= summer =")
    for y, x, age in dead:
        score[y][x] += age // 2


# 가을
# 나이가 5의 배수인 나무의 인접 8칸에 나이가 1인 나무 추가
def fall(agefive):
    # print("= fall =")
    for y, x in agefive:
        for i in range(8):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < N and 0 <= nx < N:
                trees[ny][nx].append(1)


# 겨울
# 전체 땅에 양분 추가 A matrix
def winter():
    # print("= winter =")
    for y in range(N):
        for x in range(N):
            score[y][x] += A[y][x]


def print_tree():
    print("----- tree -----")
    for row in trees:
        for elem in row:
            print(elem, end=" ")
        print()

def print_score():
    print("----- score -----")
    for row in score:
        for elem in row:
            print(elem, end=" ")
        print()


for _ in range(K):
    dead = []
    agefive = []

    spring(agefive)
    summer(dead)
    fall(agefive)
    winter()


answer = 0
for row in trees:
    for arr in row:
        answer += len(arr)

print(answer)




