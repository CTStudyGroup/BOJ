N = int(input())

matrix = []
for _ in range(N):
    matrix.append(input().strip().split())

def calculate(path):
    tmp = path[:]
    result = int(tmp.pop(0))
    while tmp:
        operator = tmp.pop(0)
        post = int(tmp.pop(0))
        if(operator == "*"):
            result *= post
        elif(operator == "+"):
            result += post
        else:
            result -= post
    return result

maximum = -10**9
minimum = 10**9
dx = [1, 0]
dy = [0, 1]
def backtrack(currentX, currentY,depth, path):
    global maximum
    global minimum
    if(depth == 2*N-1):
        result = calculate(path)
        maximum = max(maximum, result)
        minimum = min(minimum, result)
        return

    for dir in range(2):
        nx = currentX + dx[dir]
        ny = currentY + dy[dir]

        if(nx < N and ny < N):
            path.append(matrix[ny][nx])
            backtrack(nx, ny, depth + 1, path)
            path.pop(-1)

backtrack(0,0,1,[matrix[0][0]])
print(maximum, minimum)

