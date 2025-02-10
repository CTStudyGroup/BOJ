r1, c1, r2, c2 = map(int, input().split())
K = 5000
N = K*2+1
matrix = [[0 for _ in range(N)] for _ in range(N)]

# d 0:상, 1:좌, 2:하, 3:우
dd = [1, 2, 3, 0]

r = N//2
c = N//2
d = 3
num = 1
cnt = 1
curr_cnt = -1

while True:
    matrix[r][c] = num
    curr_cnt += 1
    num += 1
    # print("r:", r, ",c:", c, ",curr_cnt:", curr_cnt, ", cnt:", cnt, ",d:", d)
    if curr_cnt == cnt:  # 방향 전환
        d = dd[d]
        curr_cnt = 0
        if d == 1 or d == 3:
            cnt += 1

    if d == 0:
        r, c = r-1, c
    elif d == 1:
        r, c = r, c-1
    elif d == 2:
        r, c = r+1, c
    elif d == 3:
        r, c = r, c+1

    if r < 0 or r >= N or c < 0 or c >= N:
        break

num_len = len(str(num-1))

for r in range(r1+K, r2+K+1):
    for c in range(c1+K, c2+K+1):
        print("{:>{}}".format(matrix[r][c], num_len), end=" ")
    print()
