import sys
import heapq
input = sys.stdin.readline

Q = int(input())

# 각 이름마다 가치 높은 것 b개 뽑아야 함
# 이름별 우선순위큐
_dict = {}
answer = 0

for _ in range(Q):
    cmd = list(input().split())
    name = cmd[1]
    if cmd[0] == "1":
        nums = list(map(int, cmd[3:]))

        if name not in _dict:  # 우선순위큐 초기화
            _dict[name] = [-x for x in nums]
            heapq.heapify(_dict[name])

        else:
            heap = _dict[name]
            for x in nums:
                heapq.heappush(heap, -x)
    else:
        b = int(cmd[2])
        if name not in _dict:
            continue

        heap = _dict[name]
        for _ in range(b):
            if not heap:
                break
            answer -= heapq.heappop(heap)

print(answer)
