def magic(d, s, N, A, coors):    
    direction = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
    clouds = []
    # Move Clouds
    for x, y in coors:
        dx, dy = direction[d]
        r, c = (x+(dx*s))%N, (y+(dy*s))%N
        A[r][c] += 1
        clouds.append((r, c))

    # Copy
    for r, c in clouds:
        for dr, dc in [(1, 1), (-1, 1), (-1, -1), (1, -1)]:
            nr, nc = r+dr, c+dc
            if 0<=nr<N and 0<=nc<N and A[nr][nc]>0:
                A[r][c] += 1

    # Add new Clouds
    coord_set = set(clouds)
    coordinates = []
    for i in range(N):
        for j in range(N):
            if A[i][j]>=2 and (i, j) not in coord_set:
                A[i][j] -= 2
                coordinates.append((i, j))
    return coordinates

N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
coors = [(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)]
for _ in range(M):
    d, s = map(int, input().split())
    coors = magic(d-1, s, N, A, coors)
print(sum(map(sum, A)))