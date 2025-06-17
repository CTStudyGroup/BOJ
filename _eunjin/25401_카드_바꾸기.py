import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
ans = N - 1  # 최악의 경우: 두 카드를 고정하고 나머지 모두 교체

for i in range(N):
    for j in range(i + 1, N):
        # 공차 계산
        diff = A[j] - A[i]
        dist = j - i

        # 정수 공차 아니면 건너뜀
        if diff % dist != 0:
            continue

        d = diff // dist
        # 첫 항 계산
        a1 = A[i] - d * i

        # 변경 필요한 카드 수 세기
        cnt = 0
        for k in range(N):
            if A[k] != a1 + d * k:
                cnt += 1

        ans = min(ans, cnt)

print(ans)
