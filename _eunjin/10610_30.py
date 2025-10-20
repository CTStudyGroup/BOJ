N = list(input())

# 30의 배수 = 10의 배수 이면서 3의 배수여야 함

if '0' not in N:  # 10의 배수가 아닌 경우
    print(-1)
    exit()

sm = 0
for i in range(len(N)):
    sm += int(N[i])

if sm % 3 != 0:  # 3의 배수가 아닌 경우
    print(-1)
    exit()

# 30의 배수인 경우, 주어진 숫자 내림차순 정렬
print(''.join(sorted(N, reverse=True)))
