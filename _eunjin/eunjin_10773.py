# 입력 받기
K = int(input())

arr = []
for _ in range(K):
    n = int(input())
    if n == 0:
        arr.pop()
    else:
        arr.append(n)

print(sum(arr))
