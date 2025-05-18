N, K = map(int, input().split())

n = 0
l = 0
while n < N:
    n += 1
    st = str(n)
    if l + len(st) >= K:
        print(st[K - l - 1])
        exit()
    l += len(st)

print(-1)
