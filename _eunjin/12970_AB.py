N, K = map(int, input().split())

# 불가능한 경우
mx_cnt = 0  # 가능한 최대 (A,B) 쌍의 개수
for i in range(N // 2 + 1):
    mx_cnt = max(mx_cnt, i * (N - i))

if mx_cnt < K:
    print(-1)
    exit()

S = ['B'] * N
cnt = 0

while cnt != K:
    idx = N - 1  # A가 들어갈 인덱스

    # 가장 뒤 문자를 A로 바꾸기
    cnt -= S.count('A')  # 가장 마지막 B를 A로 바꾸면 앞 A 개수만큼 (A, B)쌍의 수가 줄어듦
    S[idx] = 'A'

    while idx > 0 and S[idx - 1] == 'B' and cnt != K:
        # A를 한칸 앞으로 당기기
        S[idx] = 'B'
        idx -= 1
        S[idx] = 'A'
        cnt += 1

print(''.join(S))
