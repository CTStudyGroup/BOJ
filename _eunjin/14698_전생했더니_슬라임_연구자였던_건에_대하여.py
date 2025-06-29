import sys
import heapq
input = sys.stdin.readline

# 2,3,8,10,14
# 2*3, 8*10
# => 6,80,14
# 6*14
# => 84, 80
# 84*80
# 6 * 80 * 84 * 6720

# 앞에서부터 두개씩 쌍으로 만들기, 홀수 개면 제일 뒤에거 놔두기

def solve(slime):
    answer = 1
    heapq.heapify(slime)  # 우선순위큐로 변환

    while len(slime) > 1:
        a = heapq.heappop(slime)
        b = heapq.heappop(slime)
        answer *= a * b
        heapq.heappush(slime, a * b)

    return answer

T = int(input())
MOD = 1000000007

for _ in range(T):
    N = int(input())
    slime = list(map(int, input().split()))
    slime.sort()
    print(solve(slime) % MOD)


# 틀린 풀이
# def solve(slime):
#     answer = 1

#     while len(slime) > 1:
#         new_slime = []
#         for i in range(0, len(slime), 2):
#             if i == len(slime) - 1:  # 마지막 슬라임
#                 new_slime.append(slime[i])
#                 continue
#             energy = slime[i] * slime[i + 1]
#             answer *= energy
#             new_slime.append(energy)

#         new_slime.sort()
#         # print("new slime:", new_slime)
#         slime = new_slime

#     return answer
