N = int(input())
T = list(map(int, input().split()))
T.sort()

answer = 0

if N % 2 == 0:  # 짝수개인 경우 양 끝을 선택
    for i in range(0, N//2):
        answer = max(answer, T[i]+T[N-i-1])
else:  # 홀수개인 경우 (0 ~ N-2번째 쌍 중의 최댓값)과 (제일 끝 값 1개) 중 최댓값
    for i in range(0, N//2):
        answer = max(answer, T[i]+T[N-i-2])
    answer = max(answer, T[N-1])
print(answer)
