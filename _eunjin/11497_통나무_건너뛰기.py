import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    L = list(map(int, input().split()))

    L.sort()

    mx = 0

    # mx = max(mx, L[-1] - L[-3])  # 가장 큰 3개끼리의 차이
    # mx = max(mx, L[-2] - L[-4])  # 2번쨰로 큰 것과 4번째로 큰 것의 차이
    # mx = max(mx, L[-3] - L[-5])  # 3번쨰로 큰 것과 5번째로 큰 것의 차이

    for i in range(1, N - 1):
        mx = max(mx, L[-i] - L[-i - 2])

    print(mx)
