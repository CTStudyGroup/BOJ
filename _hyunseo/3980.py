import sys

input =sys.stdin.readline

def dfs( last_chosen, sum_skills, chosen) :
    
    global answer
    if last_chosen == 10 :
        answer = max(answer, sum_skills)
        return
    nxt = last_chosen + 1
    # 다음 선수 가능한 조합 모두 dfs탐색
    for skill in range(11) :
        # 만약 이미 선택되었다면 무시
        if skill in chosen : continue
        # 스킬이 0이 아닌 경우에만 탐색
        if skills[nxt][skill] != 0 :
            sum_skills += skills[nxt][skill]
            chosen.add(skill)
            dfs(nxt, sum_skills, chosen)
            sum_skills -= skills[nxt][skill]
            chosen.remove(skill)
    return

def solve(skills) :
    answer = 0
    for tmp in range(11) :
        if skills[0][tmp] != 0 :
            dfs(0, skills[0][tmp], {tmp})



T = int(input())  # testcase

for _ in range(T) :
    skills = []
    answer = 0
    for _ in range(11) :
        skills.append(list(map(int, input().split())))
    solve(skills)
    print(answer)
