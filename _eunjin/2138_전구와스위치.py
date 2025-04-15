N = int(input())

given = list(map(int, list(input())))
target = list(map(int, list(input())))

d = [1, 0]

# 첫번째 스위치 누르는 경우
lights = given[:]
cnt1 = 1
lights[0], lights[1] = d[lights[0]], d[lights[1]]
for i in range(1, N):
    if lights[i - 1] != target[i - 1]:
        lights[i - 1] = d[lights[i - 1]]
        lights[i] = d[lights[i]]
        if i + 1 < N:
            lights[i + 1] = d[lights[i + 1]]
        cnt1 += 1

if lights[-1] != target[-1]:
    cnt1 = -1

# 첫번째 스위치 안누르는 경우
lights = given[:]
cnt2 = 0
for i in range(1, N):
    if lights[i - 1] != target[i - 1]:
        lights[i - 1] = d[lights[i - 1]]
        lights[i] = d[lights[i]]
        if i + 1 < N:
            lights[i + 1] = d[lights[i + 1]]
        cnt2 += 1

if lights[-1] != target[-1]:
    cnt2 = -1

if cnt1 == -1 and cnt2 == -1:
    print(-1)
elif cnt1 == -1:
    print(cnt2)
elif cnt2 == -1:
    print(cnt1)
else:
    print(min(cnt1, cnt2))
