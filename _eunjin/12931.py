N = int(input())
B = list(map(int, input().split()))

# 그리디
# 1이 있으면 2배 불가: 전체 sum
# B 전체를 2로 나누면서 cnt+1
# B에 1이 아닌 홀수 있으면 걔만 -1시키고 cnt+1

answer = 0

while True:
    for i in range(N):
        if B[i] % 2 == 1:
            B[i] -= 1
            answer += 1

    if sum(B) == 0:
        break
    for i in range(N):
        B[i] = B[i] // 2
    answer += 1

print(answer)
