from itertools import permutations

# 입력 받기
N = int(input())

num = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

# 숫자 3개의 모든 조합 생성
perms = []
for elem in list(permutations(num, 3)):
    perms.append(''.join(elem[0:3]))

# 결과적으로 가능한 조합들만을 저장할 리스트
result_list = perms[:]

qna = {}

# 질문과 답변 저장
for _ in range(N):
    q, s, b = input().split()
    s = int(s)
    b = int(b)
    qna[q] = [s, b]


def countBall(ans, inp):
    result = 0
    for i in range(0, 3):
        if (ans[i] in inp and ans[i] != inp[i]):  # strike의 개수는 제외해야 하므로
            result += 1
    return result


def countStrike(ans, inp):
    result = 0
    for i in range(0, 3):
        if(ans[i] == inp[i]):
            result += 1
    return result


# 전체 조합에서 질문과 답변 바탕으로 불가능한 조합을 제거
# 각 후보 조합마다 qna를 다 돌면서 얘가 가능한 애인지 아닌지 판단
for hubo in perms:
    for key in qna:
        # 각 hubo와 key를 비교해 strike와 ball 개수 카운트
        strikes = countStrike(key, hubo)
        balls = countBall(key, hubo)
        # strike와 ball 개수가 답변과 맞지 않으면 후보가 아니므로 결과 리스트에서 제거
        if(strikes != qna[key][0] or balls != qna[key][1]):
            if(hubo in result_list):
                result_list.remove(hubo)

print(len(result_list))
