N, K = map(int, input().split())

# 이진수로 변환했을 때 1의 개수 = 물병의 개수

answer = 0

while True:
    cnt = bin(N).count("1")
    if cnt <= K:
        break
    N += 1
    answer += 1

print(answer)
