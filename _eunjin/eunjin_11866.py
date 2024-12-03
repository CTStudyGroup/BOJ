# 입력 받기
N, K = map(int, input().split())

arr = [i for i in range(1, N+1)]

idx = K-1
result = []
while arr:
    result.append(arr.pop(idx))
    if len(arr) > 0:
        idx = (idx+K-1) % (len(arr))

print("<"+', '.join(map(str, result))+">")
