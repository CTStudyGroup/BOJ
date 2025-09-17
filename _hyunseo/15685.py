
# 하나의 드래콘 커브 세대 더하기
def add_curve(curr) :
    base = curr[-1]
    
    new_curr = list(curr)
    bx, by = base
    for c in curr[::-1] :
        cx, cy = c
        n_x = bx - (cy-by)
        n_y = by +(cx-bx)

        grid[n_y][n_x] = 'x'
        new_curr.append((n_x, n_y))
    return new_curr
    
 # 주어진 시작 좌표와, 방향, generation으로 주어진 드래곤 커브 구하기
def draw_dragon_curve(x, y, d, g) :
    grid[y][x] = 'x'
    tx, ty = 0, 0
    if d == 0 :
        tx, ty = x + 1, y
    if d == 1 :
        tx, ty = x, y - 1 
    if d == 2 :
        tx, ty = x -1, y
    if d == 3 :
        tx, ty = x, y + 1
    grid[ty][tx] = 'x'
    curr = []
    curr.append((x, y))
    curr.append((tx, ty))
    for _ in range(g) :
        curr = add_curve(curr)

# 문제 요건 정사각형 구하기
def count_rec():
    count = 0
    for i in range(100) :
        for j in range(100) :
            if grid[i][j] == 'x' :
                if grid[i+1][j] == 'x' and grid[i][j+1] == 'x' and grid[i+1][j+1] == 'x' :
                    count += 1
    return count

N = int(input())
grid = [['']*101 for _ in range(101)]
for n in range(N) :
    x, y, d, g = map(int, input().split())
    draw_dragon_curve(x, y, d, g)

print(count_rec())
