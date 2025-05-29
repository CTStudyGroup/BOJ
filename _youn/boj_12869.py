import sys
from itertools import permutations
from collections import deque

def bfs(SCV):
    visited = [[[0]*61 for _ in range(61)] for _ in range(61)]
    queue = deque([SCV])
    visited[SCV[0]][SCV[1]][SCV[2]] = 0

    while queue:
        scv1, scv2, scv3 = queue.popleft()

        for a, b, c in permutations([9,3,1]):
            c_scv1, c_scv2, c_scv3 = max(0, scv1 - a), max(0, scv2 - b), max(0, scv3 - c)
            if not visited[c_scv1][c_scv2][c_scv3]:
                queue.append((c_scv1, c_scv2, c_scv3))
                visited[c_scv1][c_scv2][c_scv3] = visited[scv1][scv2][scv3] + 1
    return visited[0][0][0]

N = int(sys.stdin.readline())
SCV = list(map(int, sys.stdin.readline().split()))+[0]*(3-N)
print(bfs(SCV))
