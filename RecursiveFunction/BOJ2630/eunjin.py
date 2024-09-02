# 나의 풀이

def recursion(N, arr):
  # 1의 존재 여부
    blueExists = False
    for row in arr:
        if 1 in row:
            blueExists = True
            break

    # 0의 존재 여부
    whiteExists = False
    for row in arr:
        if 0 in row:
            whiteExists = True
            break

    if(N == 1):
        if(blueExists):
            global blue
            blue += 1
        else:
            global white
            white += 1
        return
    elif(blueExists and not whiteExists):
        blue += 1
        return
    elif(not blueExists and whiteExists):
        white += 1
        return
    else:
        recursion(N//2, [row[0:N//2] for row in arr[0:N//2]])
        recursion(N//2, [row[N//2:N] for row in arr[0:N//2]])
        recursion(N//2, [row[0:N//2] for row in arr[N//2:N]])
        recursion(N//2, [row[N//2:N] for row in arr[N//2:N]])


blue = 0
white = 0

N = int(input())

array = []

for _ in range(N):
    row = list(map(int, input().split()))
    array.append(row)

recursion(N, array)

print(white)
print(blue)

# 다른 풀이
# import sys

# N = int(sys.stdin.readline())
# paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# result = []

# def solution(x, y, N) :
#   color = paper[x][y]
#   for i in range(x, x+N) :
#     for j in range(y, y+N) :
#       if color != paper[i][j] :
#         solution(x, y, N//2)
#         solution(x, y+N//2, N//2)
#         solution(x+N//2, y, N//2)
#         solution(x+N//2, y+N//2, N//2)
#         return
#   if color == 0 :
#     result.append(0)
#   else :
#     result.append(1)


# solution(0,0,N)
# print(result.count(0))
# print(result.count(1))
