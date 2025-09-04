from collections import deque
start, end, death, N = map(int, input().split())

# 큐로 완전 구현 문제처럼 풀려고 했으나.. 그거 안될듯
# 그냥 태어난지 n일차(0~death)된 짚신벌레 수를 각각 저장할 수 있을지 => 안됨 O(10000 * N)

# dp인가.....
born = [0] * (N + 1)  # N일차에 태어난 짚신벌레 수
born[0] = 1

# start ~ end일차 사이에 태어난 개체수 구해야함 = 특정 구간 개체수 합
born_psum = [0] * (N + 1)  # N일차까지 태어난 짚신벌레 수 누적합
born_psum[0] = 1

live = [0] * (N + 1)  # N일차에 살아있는 짚신벌레 수
live[0] = 1
MOD = 1000

for i in range(1, N + 1):
    live[i] = live[i - 1] % MOD
    born_psum[i] += born_psum[i - 1] % MOD
    if i >= death:
        live[i] -= born[i - death]  # (i-death)일차에 태어난 개체수 차감

    if i >= end:  # i-end일차 이후부터 i-start일차까지에 태어난 개체로부터 새 개체 생성
        born[i] = (born_psum[i - start] - born_psum[i - end]) % MOD
        live[i] += born[i] % MOD
        born_psum[i] = (born_psum[i - 1] + born[i]) % MOD
    elif i >= start:  # i-start일차 이후 태어난 개체로부터 새 개체 생성
        born[i] = born_psum[i - start] % MOD
        live[i] += born[i] % MOD
        born_psum[i] = (born_psum[i - 1] + born[i]) % MOD

print(live[N] % MOD)
