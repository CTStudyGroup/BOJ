import sys
input = sys.stdin.readline

# # 입력 받기
# N = int(input())
# matrix = [[0, 0, 0]]
# for _ in range(N):
#     matrix.append(list(map(int, input().split())))

# INF = int(1e6)

# mindp = [[INF]*3 for _ in range(N+1)]
# maxdp = [[-1]*3 for _ in range(N+1)]

# mindp[0][0] = matrix[0][0]
# mindp[0][1] = matrix[0][1]
# mindp[0][2] = matrix[0][2]

# maxdp[0][0] = matrix[0][0]
# maxdp[0][1] = matrix[0][1]
# maxdp[0][2] = matrix[0][2]

# for i in range(1, N+1):
#     mindp[i][0] = min(mindp[i-1][0], mindp[i-1][1])+matrix[i][0]
#     maxdp[i][0] = max(maxdp[i-1][0], maxdp[i-1][1])+matrix[i][0]

#     mindp[i][1] = min(mindp[i-1][0], mindp[i-1][2])+matrix[i][1]
#     maxdp[i][1] = max(maxdp[i-1][0], maxdp[i-1][2])+matrix[i][1]

#     mindp[i][2] = min(mindp[i-1][2], mindp[i-1][1])+matrix[i][2]
#     maxdp[i][2] = max(maxdp[i-1][2], maxdp[i-1][1])+matrix[i][2]

# # print(maxdp)
# # print(mindp)
# print(max(maxdp[N]), min(mindp[N]))

# 입력 받기
N = int(input())

scores = list(map(int, input().split()))
mindp = scores
maxdp = scores

for _ in range(N-1):
    scores = list(map(int, input().split()))

    mindp = [min(mindp[0], mindp[1])+scores[0], min(mindp) +
             scores[1], min(mindp[1], mindp[2])+scores[2]]

    maxdp = [max(maxdp[0], maxdp[1])+scores[0], max(maxdp) +
             scores[1], max(maxdp[1], maxdp[2])+scores[2]]
    # print("mindp:", mindp)
    # print("maxdp:", maxdp)

print(max(maxdp), min(mindp))
