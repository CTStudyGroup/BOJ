import heapq
import sys
input = sys.stdin.readline

N = int(input())

# 우선순위큐 2개로 어려운순, 쉬운순으로 문제 저장
# 각 문제별 삭제 여부를 해시로 저장? 1~100: 존재함, 0: 삭제됨
maxq = []
minq = []
_dict = {}

for _ in range(N):
    P, L = map(int, input().split())
    heapq.heappush(maxq, (-L, -P))
    heapq.heappush(minq, (L, P))
    _dict[P] = L

M = int(input())
for _ in range(M):
    cmd = list(input().split())
    if cmd[0] == "add":
        P, L = int(cmd[1]), int(cmd[2])
        heapq.heappush(maxq, (-L, -P))
        heapq.heappush(minq, (L, P))
        _dict[P] = L
    elif cmd[0] == "recommend":
        if cmd[1] == "1":  # 어려운 문제 출력
            while True:  # 삭제되지 않은 가장 어려운 문제 나올 때까지
                l, p = heapq.heappop(maxq)
                if _dict[-1 * p] == -1 * l:
                    print(-1 * p)
                    heapq.heappush(maxq, (l, p))
                    break
        else:  # 쉬운 문제 출력
            while True:  # 삭제되지 않은 가장 쉬운 문제 나올 때까지
                l, p = heapq.heappop(minq)
                if _dict[p] == l:
                    print(p)
                    heapq.heappush(minq, (l, p))
                    break
    else:  # solved
        _dict[int(cmd[1])] = 0
