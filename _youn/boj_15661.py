import sys

def getAbility(visited, S, N):
    teamS, teamL = 0, 0
    for i in range(N):
        for j in range(i+1, N):
            if visited[i] and visited[j]:
                teamS += (S[i][j] + S[j][i])
            elif not visited[i] and not visited[j]:
                teamL += (S[i][j] + S[j][i])
    return abs(teamS-teamL)

def solve(start, visited, depth, N, S):
    if depth == 0: # base case
        global ans
        ans = min(ans, getAbility(visited, S, N))
        return

    for i in range(start, N):
        if not visited[i]:
            visited[i] = True
            solve(i+1, visited, depth-1, N, S)
            visited[i] = False

N = int(sys.stdin.readline())
S = [list(map(int, sys.stdin.readline().split()))\
     for _ in range(N)]
ans = float('inf')
visited = [False]*N
visited[0] = True
for n in range(1, N//2+1):
    solve(1, visited, n, N, S)
print(ans)