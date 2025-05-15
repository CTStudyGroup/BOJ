def format_time(t):
    return f"{t // 60:02d}:{t % 60:02d}"

def solve(goals):
    ans = [0, 0]
    curr = 48*60

    for team, time in goals[::-1]:
        if team!=-1: ans[team] += (curr-time)
        curr = time
    
    print('\n'.join(map(format_time, ans)))

N = int(input())
goals = []
score = [0, 0]
for _ in range(N):
    team, time = input().split()
    minute, second = map(int, time.split(":"))

    team_idx = int(team)-1
    score[team_idx]+=1
    
    if score[0]>score[1]: team = 0
    elif score[0]<score[1]: team = 1
    else: team = -1
    goals.append((team, minute*60+second))
solve(goals)