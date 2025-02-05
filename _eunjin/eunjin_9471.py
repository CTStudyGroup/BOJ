def fisano(n):
    ret = 0
    mod1, mod2 = 0, 1
    while True:
        mod1, mod2 = mod2, (mod1+mod2) % n
        ret += 1
        if mod1 == 0 and mod2 == 1:
            break
    return ret


T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    print(N, fisano(M))
