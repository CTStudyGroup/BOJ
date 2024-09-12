# 입력 받기

N = int(input())

current = 1000-N
cnt = 0

cnt += current // 500
current %= 500

cnt += current // 100
current %= 100

cnt += current // 50
current %= 50

cnt += current // 10
current %= 10

cnt += current // 5
current %= 5

cnt += current // 1
current %= 1

print(cnt)
