# N, K, B = map(int, input().split())

# err = list(int(input()) for _ in range(B))

# light = [1] * (N + 1)

# for x in err:
#     light[x] = 0

# answer = float('inf')

# for i in range(1, N + 1 - K):
#     # 고장나지 않은 신호등 개수
#     x = sum(light[i:i + K])
#     answer = min(answer, K - x)

# print(answer)

# 위 풀이는 시간 초과
# sum 말고 슬라이딩 윈도우로 수리할 신호등 개수 업데이트하자

N, K, B = map(int, input().split())

err = list(int(input()) for _ in range(B))

light = [1] * N

for x in err:
    light[x - 1] = 0

# print(light)

# 0 ~ K까지의 수리할 신호등 개수
cnt = K - sum(light[:K])
arr = []
arr.append(cnt)

for i in range(1, N - K + 1):
    if light[i - 1] == 0:
        cnt -= 1
    if light[i + K - 1] == 0:
        cnt += 1
    arr.append(cnt)

print(min(arr))
