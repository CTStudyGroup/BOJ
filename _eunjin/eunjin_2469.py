K = int(input())
N = int(input())
start = [chr(i) for i in range(65, 65 + K)]
target = list(input())
board = [list(input()) for _ in range(N)]

q_idx = -1

# ? 위치 찾기
for i in range(N):
    if board[i][0] == '?':
        q_idx = i
        break

# start를 시작부터 ?행 전까지 이동
for i in range(q_idx):
    for j in range(K - 1):
        if board[i][j] == '-':
            start[j], start[j + 1] = start[j + 1], start[j]

# target을 아래서부터 ?행 전까지 이동
bottom = target[:]
for i in range(N - 1, q_idx, -1):
    for j in range(K - 1):
        if board[i][j] == '-':
            bottom[j], bottom[j + 1] = bottom[j + 1], bottom[j]

# start -> bottom 되려면 필요한 자리 바꾸는 연산 찾기
answer = []
i = 0
while i < K - 1:
    if start[i] == bottom[i]:  # 자리 안바꿔도 되는 경우
        answer.append("*")
        i += 1
    elif start[i] == bottom[i + 1] and start[i + 1] == bottom[i]:  # 자리 바꾸는 경우
        answer.append('-')
        answer.append('*')
        i += 2
    else:  # start -> bottom이 될 수 없는 경우
        print('x' * (K - 1))
        exit()

print(''.join(answer[:K - 1]))
