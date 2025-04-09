import heapq
import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
arr.sort(key=lambda x: x[0])

# 강의실별 종료시간(T) 우선순위 큐를 두기
# S 시점마다 큐에서 종료시간(T)이 가장 이른 애를 하나 꺼내고 그게 S보다 작거나 같으면 그 강의실을 사용, T를 큐에 넣기
# 꺼낸 종료시간(T)가 S 보다 크면 S 시점에서 사용할 수 있는 남은 강의실이 없으므로 T를 큐에 추가, 꺼낸 종료시간도 다시 넣기

q = []

for S, T in arr:
    # print("---- S:", S, ", T:", T, " ----")
    # print("q:", q)
    if not q:
        heapq.heappush(q, T)
        # print("heappush T:", T)
        continue

    qt = heapq.heappop(q)
    if qt <= S:
        heapq.heappush(q, T)
        # print("heappush T:", T)
    else:
        heapq.heappush(q, qt)
        # print("heappush qt:", qt)
        heapq.heappush(q, T)
        # print("heappush T:", T)
    # print()

# print(q)
print(len(q))
