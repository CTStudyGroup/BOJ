N = int(input())

matrix = [list(map(int, input().split())) for _ in range(N)]
answer = [0, 0, 0]  # -1, 0, 1

def count2(y1, x1, y2, x2):
    c0, c1, c2 = 0, 0, 0
    for y in range(y1, y2 + 1):
        for x in range(x1, x2 + 1):
            if matrix[y][x] == 0:
                c0 += 1
            elif matrix[y][x] == 1:
                c1 += 1
            else:
                c2 += 1
    return c0, c1, c2

def divide2(y1, x1, y2, x2, n):
    c0, c1, c2 = count2(y1, x1, y2, x2)
    if (c0 != 0 and c1 == 0 and c2 == 0):  # 0으로만 이루어진 경우
        answer[1] += 1
    elif (c1 != 0 and c0 == 0 and c2 == 0):  # 1로만 이루어진 경우
        answer[2] += 1
    elif (c2 != 0 and c0 == 0 and c1 == 0):  # -1로만 이루어진 경우
        answer[0] += 1
    else:
        k = n // 3
        for y in range(y1, y2 + 1, k):
            for x in range(x1, x2 + 1, k):
                divide2(y, x, y + k - 1, x + k - 1, k)


divide2(0, 0, N - 1, N - 1, N)

print(answer[0])
print(answer[1])
print(answer[2])


# 시간 초과 풀이

# def count(matrix):
#     count0 = 0
#     count1 = 0
#     count2 = 0

#     for y in range(len(matrix)):
#         for x in range(len(matrix[y])):
#             if matrix[y][x] == 0:
#                 count0 += 1
#             elif matrix[y][x] == 1:
#                 count1 += 1
#             else:
#                 count2 += 1

#     return count0, count1, count2

# def divide(matrix, n):
#     c0, c1, c2 = count(matrix)
#     if (c0 != 0 and c1 == 0 and c2 == 0):  # 0으로만 이루어진 경우
#         answer[1] += 1
#     elif (c1 != 0 and c0 == 0 and c2 == 0):  # 1로만 이루어진 경우
#         answer[2] += 1
#     elif (c2 != 0 and c0 == 0 and c1 == 0):  # -1로만 이루어진 경우
#         answer[0] += 1
#     else:  # 숫자 섞여있는 경우
#         k = n // 3
#         for y in range(0, n, k):  # 구간
#             for x in range(0, n, k):
#                 temp_matrix = [[] for _ in range(k)]  # 쪼갠 부분 matrix
#                 for i in range(k):
#                     for j in range(k):
#                         temp_matrix[i].append(matrix[y + i][x + j])

#                 divide(temp_matrix, k)

# divide(matrix, N)

# print(answer[0])
# print(answer[1])
# print(answer[2])
