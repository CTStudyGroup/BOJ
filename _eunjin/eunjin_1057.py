import math

# 입력 받기
N, kim, lim = map(int, input().split())

if N % 2 == 0:
    N = math.ceil(math.sqrt(N))
else:
    N = math.ceil(math.sqrt(N))+1


def isPair(kim, lim):
    if kim-lim != 1 and lim-kim != 1:
        return False
    if kim < lim:
        if kim % 2 == 1:
            return True
    if lim < kim:
        if lim % 2 == 1:
            return True
    return False


for n in range(N):
    # print("n:", n, ",kim:", kim, ",lim:", lim)
    if isPair(kim, lim):
        print(n+1)
        break

    kim = math.ceil(kim/2)
    lim = math.ceil(lim/2)
