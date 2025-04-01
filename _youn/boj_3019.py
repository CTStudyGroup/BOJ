blockShape = {
    1: [[0],[0,0,0,0]],
    2: [[0,0]],
    3: [[0,0,1],[1,0]],
    4: [[1,0,0],[0,1]],
    5: [[0,0,0],[1,0],[1,0,1],[0,1]],
    6: [[0,0,0],[2,0],[0,1,1],[0,0]],
    7: [[0,0,0],[0,0],[1,1,0],[0,2]]
}

C , P = map(int, input().split())
tetris = list(map(int, input().split()))
ans = 0

for b in blockShape[P]:
    for i in range(C-len(b)+1): # start
        minVal = min(tetris[i:i+len(b)])
        diff = [tetris[i+j]-minVal for j in range(len(b))]

        if diff == b:
            ans+=1
print(ans)