N = int(input())
arr = list(map(int, input().split()))
INF = int(1e10)

# N개의 좌표마다 다른 빌딩과의 기울기 구해서 해당 빌딩 보이는지 여부 파악
# (N~자신의 기울기)보다 크거나 같은 (N~다른 빌딩 기울기) 있으면 자신은 보이지 않음
# 기울기가 기존 mx 값보다 더 커야만 해당 빌딩이 보이게 됨

# matrix[a][b] = a->b의 기울기
matrix = [[0] * N for _ in range(N)]

for i in range(N):  # N개의 좌표에 대해
    for j in range(N):  # 다른 모든 빌딩과의 기울기
        if i == j:
            continue

        matrix[i][j] = (arr[j] - arr[i]) / abs(j - i)

count = [0] * N
# 해당 좌표 기준 왼쪽 방향 탐색
for i in range(1, N):
    mn = -INF
    for j in range(i - 1, -1, -1):
        if matrix[i][j] > mn:
            mn = matrix[i][j]
            count[i] += 1

# 해당 좌표 기준 오른쪽 방향 탐색
for i in range(N - 1):
    mx = -INF
    for j in range(i + 1, N):
        if matrix[i][j] > mx:
            mx = matrix[i][j]
            count[i] += 1

print(max(count))
