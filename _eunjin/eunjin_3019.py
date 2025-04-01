C, P = map(int, input().split())
arr = list(map(int, input().split()))

# 그냥 구현? 완전탐색

block1 = [[0], [0, 0, 0, 0]]
block2 = [[0, 0]]
block3 = [[0, 0, 1], [0, -1]]
block4 = [[0, -1, -1], [0, 1]]
block5 = [[0, 0, 0], [0, 1], [0, -1, 0], [0, -1]]
block6 = [[0, 0, 0], [0, 0], [0, 1, 1], [0, -2]]
block7 = [[0, 0, 0], [0, 2], [0, 0, -1], [0, 0]]
blocks = [block1, block2, block3, block4, block5, block6, block7]

block = blocks[P - 1]

answer = 0

for b in block:  # 해당 블록의 아랫면 조합에 대해
    for i in range(C):  # 모든 열을 시작점으로 두고
        start = arr[i]
        if i + len(b) > C:
            break

        valid = True

        for j in range(len(b)):
            if start + b[j] != arr[i + j]:
                valid = False
                continue
        if valid:
            # print("start:", i, ", block:", b)
            answer += 1

print(answer)
