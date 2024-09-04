# 입력 받기
T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    result = M

    if(N == 1):
        print(M)
    else:
        for i in range(2, N+1):
            result = result*(M-i+1)//i

        print(result)
