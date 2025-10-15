# 미네랄의 모양을 그대로 출력
# 테트리스와 동일한 원리
# 한 열의 모든 값이 .이면 그 열을 삭제

# 초기 설정 ==========================
R, C = map(int, input().split(" "))

matrix = []
for row in range(R):
    new_row = input()

    seperate = []
    for col in range(C):
        seperate.append(new_row[col])

    matrix.append(seperate)

N = int(input())
height = list(map(int, input().split(" ")))

# 시작 ==========================



