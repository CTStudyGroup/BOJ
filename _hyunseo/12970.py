N, K = map(int, input().split())

n = N//2

# K가 너무 커서 불가능할 경우
if n*(N-n) < K : 
    print(-1)
    exit()
    

answer = ['B']*N
cnt = 0  #A, B 쌍의 수

while cnt != K :
    idx = N-1
    cnt -= answer.count('A')
    answer[idx] = 'A'
    while idx > 0 and answer[idx-1] == 'B' and cnt != k :
        answer[idx] = 'B'
        idx -= 1
        answer[idx] = 'A'
        cnt += 1
print(''.join(answer))
