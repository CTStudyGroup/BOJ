import sys
import heapq
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    K = int(input())
    maxq = []  # 최대힙,음수로 바꿔 저장
    minq = []  # 최소힙
    valid = [1] * K  # 유효 여부
    for k in range(K):
        cmd, n = input().split()
        n = int(n)
        if cmd == "D":
            if n == 1:
                if maxq:
                    valid[heapq.heappop(maxq)[1]] = 0
            if n == -1:
                if minq:
                    valid[heapq.heappop(minq)[1]] = 0
        else:
            heapq.heappush(maxq, (-n, k))
            heapq.heappush(minq, (n, k))

        while maxq and valid[maxq[0][1]] == 0:
            heapq.heappop(maxq)
        while minq and valid[minq[0][1]] == 0:
            heapq.heappop(minq)

    if not maxq or not minq:
        print("EMPTY")
    else:
        print(-maxq[0][0], minq[0][0])
