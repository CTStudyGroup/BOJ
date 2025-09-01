# N*M의 최대값이 625이므로 백트래킹으로 완전탐색

N,M = map(int,input().split())


nemo = [[0 for _ in range(M)] for _ in range(N)]
count = 0
def backtrack(currentX, currentY):
    global count
    if(currentY == N):
        count += 1
        return
    
    # 놓을 수 있는지 없는지 판단: 2*2가 만들어지면 놓을 수 없음
    if(currentX > 0 and currentY > 0):
        if(nemo[currentY-1][currentX] and nemo[currentY-1][currentX-1] and nemo[currentY][currentX-1]):
            # 왼쪽 위, 위, 왼쪽이 모두 1인 경우 -> 여기에 놓을 수 없음
            if(currentX == M-1):
                backtrack(0, currentY + 1)
            else:
                backtrack(currentX+1, currentY)
            return

    # 이 위치에 안놓고 가는 경우
    if(currentX == M-1):
        backtrack(0, currentY + 1)
    else:
        backtrack(currentX+1, currentY)

    # 이 위치에 놓고 가는 경우
    nemo[currentY][currentX] = 1    
    if(currentX == M-1):
        backtrack(0, currentY + 1)
    else:
        backtrack(currentX+1, currentY)
    nemo[currentY][currentX] = 0

backtrack(0,0)
print(count)