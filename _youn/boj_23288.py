from collections import deque

class GAME:
    def __init__(self):
        # Game-Related
        self.N, self.M, self.K = map(int, input().split())
        self.board = [list(map(int, input().split())) for _ in range(self.N)]
        self.score = 0
        # Dice-Related
        self.dice = [1, 6, 2, 5, 3, 4] 
        self.d = 0 # direction

    # Dice-Related: State of the Dice
    def rollthedice(self): # update state of dice
        top, bottom, north, south, east, west  = self.dice
        if self.d==0: self.dice = [west, east, north, south, top, bottom] # east
        elif self.d==1: self.dice = [east, west, north, south, bottom, top] # west
        elif self.d==2: self.dice = [north, south, bottom, top, east, west] # south
        else: self.dice = [south, north, top, bottom, east, west] # north

    # Game-Related: Movement of the Dice
    def check(self, x, y): # check range of index
        return 0<=x<self.N and 0<=y<self.M

    def bfs(self, start, v): # for blocks with same val
        count = 1
        queue = deque([start])
        visited = [[False]*self.M for _ in range(self.N)]
        visited[start[0]][start[1]] = True
 
        while queue:
            x, y = queue.popleft()
            
            for dx, dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                nx, ny = x+dx, y+dy
                if self.check(nx, ny) and not visited[nx][ny] and self.board[nx][ny] == v:
                    visited[nx][ny] = True
                    count +=1
                    queue.append((nx, ny))
        return count

    def getDirection(self, A, B): # get next direction
        clockwise = {0: 2, 1: 3, 2: 1, 3: 0}
        anti_clockwise = {0: 3, 1: 2, 2: 0, 3: 1}
        if A>B: self.d = clockwise[self.d] 
        elif A<B: self.d = anti_clockwise[self.d]

    def start(self): # game start!
        movement = {0: (0,1), 1:(0,-1), 2:(1,0), 3:(-1,0)} # dir#: (dx, dy)
        x, y = 0, 0
        for _ in range(self.K): 
            dx, dy = movement[self.d]

            if not self.check(x+dx, y+dy): # oppisite direction
                self.d = self.d + 1 if self.d % 2 == 0 else self.d - 1
                dx, dy = movement[self.d]
            self.rollthedice()
            x, y = x+dx, y+dy

            v = self.board[x][y]
            count = self.bfs((x, y), v)
            self.score += count*v
            
            # get next direction
            A, B = self.dice[1], self.board[x][y]
            print(self.d,self.dice)
            if A != B:
                self.getDirection(A, B)

g = GAME()
g.start()
print(g.score)