# 입력 받기
A, B, C = map(int, input().split())


def div(a, b, c):
    if b == 1:
        return a % c
    else:
        k = div(a, b//2, c)
        if b % 2 == 0:
            return (k*k) % c
        else:
            return (k*k*a) % c


print(div(A, B, C))
