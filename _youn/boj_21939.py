import sys
import heapq

def clean(heap, problem, is_max=False):
    while heap:
        lv, id = heap[0]
        real_lv = -lv if is_max else lv
        real_id = -id if is_max else id
        if real_id not in problem or problem[real_id]!=real_lv:
            heapq.heappop(heap)
        else: break

def recommend(args, minheap, maxheap, problem):
    c = int(args[0])
    if c == 1:
        clean(maxheap, problem, is_max=True)
        print(-maxheap[0][1])
    else:
        clean(minheap, problem)
        print(minheap[0][1])

def add(args, minheap, maxheap, problem):
    id, lv = map(int, args)
    problem[id] = lv
    heapq.heappush(minheap, (lv, id))
    heapq.heappush(maxheap, (-lv, -id))

def solved(args, minheap, maxheap, problem):
    id = int(args[0])
    if id in problem:
        del problem[id]

# Input
N = int(sys.stdin.readline())
minheap, maxheap = [], []
problem = {}
for _ in range(N):
    id, lv = map(int, sys.stdin.readline().split())
    problem[id] = lv
    heapq.heappush(minheap, (lv, id))
    heapq.heappush(maxheap, (-lv, -id))

# Command
M = int(sys.stdin.readline())
system_ver1 = {'recommend': recommend, 'add': add, 'solved': solved}
for _ in range(M):
    cmd = sys.stdin.readline().split()
    system_ver1[cmd[0]](cmd[1:], minheap, maxheap, problem)