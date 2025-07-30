N, M = map(int, input().split())
guitars = []

for _ in range(N):
    _, stats = input().split()
    guitars.append(stats)

# N이 10이라서 완전탐색 가능

def backtracking(n):
    if n == N:
        # 사용하는 기타의 stats로 연주 가능한 곡 개수 구하기
        able = [False] * M

        for u in used:
            for i in range(len(guitars[u])):
                if guitars[u][i] == 'Y':
                    able[i] = True

        able_cnt = 0
        for a in able:
            if a:
                able_cnt += 1

        arr.append((able_cnt, len(used)))  # arr에 (연주가능한 곡, 필요한 기타 개수) 추가

        return

    backtracking(n + 1)  # n번째 기타 사용 안하는 경우

    # n번째 기타 사용 하는 경우
    used.append(n)
    backtracking(n + 1)
    used.pop()


arr = []  # (연주가능한 곡, 필요한 기타 개수)의 리스트
used = []
backtracking(0)

arr.sort(key=lambda x: [-x[0], x[1]])

if arr[0][0] == 0:  # 연주 가능한 곡 없는 경우
    print(-1)
else:
    print(arr[0][1])
