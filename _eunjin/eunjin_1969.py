import sys
input = sys.stdin.readline

# 입력 받기
N, M = map(int, input().split())

arr = [input().rstrip() for _ in range(N)]

result = []
dist = 0
for m in range(M):
    cnt = [0, 0, 0, 0]  # A, C, G, T
    for n in range(N):
        char = arr[n][m]
        if char == "A":
            cnt[0] += 1
        if char == "C":
            cnt[1] += 1
        if char == "G":
            cnt[2] += 1
        if char == "T":
            cnt[3] += 1

    max_value = cnt[0]
    idx = 0
    for i in range(4):
        if cnt[i] > max_value:
            max_value = cnt[i]
            idx = i

    if idx == 0:
        result.append("A")
    if idx == 1:
        result.append("C")
    if idx == 2:
        result.append("G")
    if idx == 3:
        result.append("T")

    dist += N-cnt[idx]

print(''.join(result))
print(dist)
