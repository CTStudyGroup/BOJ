N = int(input())
U = []
for _ in range(N) :
    U.append(int(input()))

# 3수를 골라서 더했을 때, 답이  U에 포함되어 있고, 이 경우 가장 큰 d
U.sort()

# 두 수 합을 모두 기록
sum_2 = set()
for i in range(N):
    for j in range(i, N):
        sum_2.add(U[i] + U[j])
        
# d = U[k] 인 값부터 큰 순서로 체크
for k in range(N-1, -1, -1):
    d = U[k]
    for i in range(N):
        # d - U[i]가 두 수 합으로 가능?
        if (d - U[i]) in sum_2:
            print(d)
            exit()
