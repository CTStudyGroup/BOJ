import heapq
import sys
input = sys.stdin.readline

# 제일 작은거 2개 합하고 다시 큐에 넣기
def solve():
    heapq.heapify(size)
    answer = 0

    while len(size) > 1:
        s1 = heapq.heappop(size)
        s2 = heapq.heappop(size)
        answer += s1 + s2
        heapq.heappush(size, s1 + s2)

    print(answer)


T = int(input())
for _ in range(T):
    K = int(input())
    size = list(map(int, input().split()))
    solve()
