# 입력 받기
N = int(input())
arr = []
for _ in range(N):
    x, y = map(int, input().split())
    arr.append((x, y))


sorted_arr = sorted(arr)

for elem in sorted_arr:
    print(elem[0], elem[1])
