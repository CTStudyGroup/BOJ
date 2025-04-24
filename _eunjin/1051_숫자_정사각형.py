import sys
input = sys.stdin.readline

N, M = map(int, input().split())
matrix = [list(map(int, list(input().strip()))) for _ in range(N)]

# 시간복잡도 확인 = 40425
# 완전탐색

X = min(N, M)

for i in range(X, 1, -1):  # 정사각형 크기를 X부터 줄여가면서 탐색
    for y in range(0, N - i + 1):  # 행 시작 지점
        for x in range(0, M - i + 1):  # 열 시작 지점
            # print("i:", i, ", y:", y, ", x:", x)
            # 네 꼭짓점 비교
            p1 = matrix[y][x]
            p2 = matrix[y][x + i - 1]
            p3 = matrix[y + i - 1][x]
            p4 = matrix[y + i - 1][x + i - 1]

            if p1 == p2 and p2 == p3 and p3 == p4:
                print(i * i)
                exit()

print(1)
