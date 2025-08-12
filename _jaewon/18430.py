# import sys
# input = sys.stdin.readline

# rows, cols = map(int, input().split())
# matrix = []

# for row in range(rows):
#     matrix.append(list(map(int, input().split())))

# def boo(centerX, centerY, visited):
#     # 4가지 shape
#     # [좌, 하], [좌, 상], [우, 하], [우, 상]
#     shapes = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
#     maximum = 0

#     for shape in shapes:
#         total = 0
#         nx = centerX + shape[0]
#         ny = centerY + shape[1]

#         visited = []
#         for r in range(rows):
#             visited.append(visited[r][:])

#         if((0<=nx<cols) and (0<=ny<rows)):
#             if(visited[ny][centerX] == 0 and visited[centerY][nx] == 0):
#                 total += matrix[centerY][centerX] * 2 + matrix[ny][centerX] + matrix[centerY][nx]
#                 visited[centerY][centerX] = 1
#                 visited[ny][centerX] = 1
#                 visited[centerY][nx] = 1
        
#         # 그 다음 부메랑 찾아가기
#         flag = 0
#         for row in range(centerY, rows):
#             for col in range(cols):
#                 if (row == centerY and col <= centerX):
#                     continue

#                 if (visited[row][col] == 0):
#                     total += boo(col, row, visited)
#                     flag = 1
#                     break
#             if(flag):
#                 break
#         maximum = max(maximum, total)
        
#     return maximum

# visited = [[0 for _ in range(cols)] for _ in range(rows)]
# print(boo(0, 0, visited))

import sys
input = sys.stdin.readline

rows, cols = map(int, input().split())
matrix = []

for row in range(rows):
    matrix.append(list(map(int, input().split())))

def boo(centerX, centerY, visited):
    # 4가지 shape
    # [좌, 하], [좌, 상], [우, 하], [우, 상]
    shapes = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    maximum = 0

    for shape in shapes:
        total = 0
        nx = centerX + shape[0]
        ny = centerY + shape[1]

        if((0<=nx<cols) and (0<=ny<rows)):
            if(visited[ny][centerX] == 0 and visited[centerY][nx] == 0):
                total = matrix[centerY][centerX] * 2 + matrix[ny][centerX] + matrix[centerY][nx]
                visited[centerY][centerX] = 1
                visited[ny][centerX] = 1
                visited[centerY][nx] = 1
        
            # 그 다음 부메랑 찾아가기
            flag = 0
            for row in range(centerY, rows):
                for col in range(cols):
                    if (row == centerY and col <= centerX):
                        continue

                    if (visited[row][col] == 0):
                        total += boo(col, row, visited)
                        flag = 1
                        break
                if(flag):
                    break
            visited[centerY][centerX] = visited[ny][centerX] = visited[centerY][nx] = False

        maximum = max(maximum, total)
        
    return maximum

visited = [[0 for _ in range(cols)] for _ in range(rows)]
print(boo(0, 0, visited))