from collections import deque
import heapq

def printBoard(board): # Print Board
    for i in range(len(board)):
        print(*board[i])

def check(x, y): # Check Index
    global N, M
    return 0<=x<N and 0<=y<M

# BFS for labeling Island
def bfs(start, board, visited, label): 
    queue = deque([start])

    while queue:
        x, y = queue.popleft()
        board[x][y] = label

        for dx, dy in [(0,1),(1,0),(-1,0),(0,-1)]:
            nx, ny = (x+dx), (y+dy)
            if check(nx, ny) and not visited[nx][ny] and board[nx][ny]==1:
                visited[nx][ny] = True
                queue.append((nx, ny))
    return board, visited

# Label Island
def findIsland(board): 
    global N, M
    visited = [[False]*M for _ in range(N)]
    label = 1

    for i in range(N):
        for j in range(M):
            if board[i][j] == 1 and not visited[i][j]:
                visited[i][j] = True
                board, visited = bfs((i,j), board, visited, label)
                label+=1
    return board, label

# Calculate Cost between Island (Node)
def findBridge(start, board, Graph): 
    v = board[start[0]][start[1]]
    
    for dx, dy in [(0,1),(1,0),(-1,0),(0,-1)]:
        (x, y), cost = start, 0
        Ocean = False

        while check(x, y): 
            if board[x][y] == 0:
                cost+=1
                Ocean = True
            elif board[x][y] not in [0, v]:
                cost > 1 and Graph[v].add((cost, board[x][y]))
                break
            elif board[x][y] == v and Ocean:
                break
            x, y = (x+dx), (y+dy)
    return Graph

# Make Graph; Graph = {Node#: [(Cost, Connected_Node#)]} 
def getBridge(board, label): 
    global N, M
    visited = [[False]*M for _ in range(N)]
    Graph = {v:set() for v in range(1, label)}

    for i in range(N):
        for j in range(M):
            if board[i][j] !=0 and not visited[i][j]:
                Graph = findBridge((i, j), board, Graph)
                visited[i][j] = True
    return Graph

# Prim Algorithm for MST (Minimum Spanning Tree)
def Prim(Graph, start = 1):
    queue = []
    visited = [True] + [False for _ in range(len(Graph))]
    heapq.heappush(queue, (0, start))
    totalCost, count = 0, 0

    while queue:
        uc, u = heapq.heappop(queue)
        if visited[u]==True: continue
        visited[u] = True
        totalCost+= uc
        count+=1

        for vc, v in Graph[u]:
            if not visited[v]:
                heapq.heappush(queue, (vc, v))

    if count == len(Graph):
        return totalCost
    return -1

# Input
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
# Solve
board, label = findIsland(board)
Graph = getBridge(board, label)
print(Prim(Graph))