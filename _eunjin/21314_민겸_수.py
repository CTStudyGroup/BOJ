# 틀린 풀이
S = input()
dt = {"K": 5, "M": 1}

if len(S) == 1:
    print(dt[S[0]])
    exit()

# 최댓값
# MK는 최대한 한번에 많이
# M은 최대한 한번에 적게 가져가야함

# 최솟값
# MK는 최대한 짧게(M,K 분리해서)
# M은 최대한 한번에 길게 가져가야함

# 최댓값: 뒤에서부터 보면서 K가 나오면 연속 M을 최대한 찾기
mx_answer = 0
curr = len(S) - 1
temp = dt[S[curr]]
x = 0

while curr >= 0:
    if S[curr] == "K":  # 연속 M구간 찾기
        if curr - 1 >= 0 and S[curr - 1] == "M":  # MK 형태이면
            start = curr - 1
            while start - 1 >= 0 and S[start - 1] == "M":
                start -= 1
            x += curr - start
            mx_answer += 5 * (10**x)
            curr = start - 1
        else:  # KK or 맨 앞이면
            mx_answer += 5 * (10**x)
            curr -= 1
    else:  # M: 1로 끊어 읽기
        mx_answer += 10**x
        curr -= 1
    x += 1

# 최솟값: 뒤에서부터 보면서 연속 M만 구간으로 치고, 나머지 전부 끊기
mn_answer = 0
curr = len(S) - 1
x = 0
while curr >= 0:
    if S[curr] == "K":  # 끊어서 읽기
        mn_answer += 5 * (10**x)
        curr -= 1
    else:  # 연속 M 구간 찾기
        start = curr
        while start - 1 >= 0 and S[start - 1] == "M":
            start -= 1
        x += curr - start
        mn_answer += 10**x
        curr = start - 1
    x += 1

print(mx_answer)
print(mn_answer)


# 정답 풀이
S = input()

# 최댓값: M은 최대한 나누고, K는 그때그때 변환
max_ans = ''
m_cnt = 0
for ch in S:
    if ch == 'M':
        m_cnt += 1
    else:  # 'K'
        if m_cnt > 0:
            max_ans += '5' + '0' * m_cnt
            m_cnt = 0
        else:
            max_ans += '5'
for _ in range(m_cnt):  # 남은 M 처리
    max_ans += '1'

# 최솟값: M은 최대한 묶고, K가 오면 M + K 묶음 처리
min_ans = ''
m_cnt = 0
for ch in S:
    if ch == 'M':
        m_cnt += 1
    else:  # 'K'
        if m_cnt > 0:
            min_ans += '1' + '0' * (m_cnt - 1)
            m_cnt = 0
        min_ans += '5'
if m_cnt > 0:
    min_ans += '1' + '0' * (m_cnt - 1)

print(max_ans)
print(min_ans)
