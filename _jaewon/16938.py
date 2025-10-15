# L <= 문제 난이도 합 <= R
# 문제 난이도[-1] - 문제 난이도[0] >= X
# 두 문제 이상 고름

# N이 15이기 때문에, 완전탐색이 가능


N, L, R, X = map(int, input().split())
hardness_list = sorted(list(map(int,input().split())))

count = 0
def backtrack(index, problems):
    global count
    if(index == len(hardness_list)):
        return

    # 1. 이 문제를 안넣는 경우
    backtrack(index + 1, problems)

    # 2. 이 문제를 넣는 경우
    current = hardness_list[index]
    problems.append(current)

    total = sum(problems)
    if(total > R):
        # 더이상 진행할 필요 없음
        # 이것보다 큰 난이도를 추가하면 어차피 불가능하기 때문
        problems.pop(-1) 
        return
    
    if(L<=total<=R and (problems[-1]-problems[0] >= X) and len(problems)>=2):
        count += 1

    backtrack(index + 1, problems)
    problems.pop(-1)

backtrack(0, [])
print(count)


