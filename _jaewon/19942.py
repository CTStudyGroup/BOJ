import sys
input = sys.stdin.readline

N = int(input())
limit = list(map(int, input().split()))

food = [list(map(int, input().split())) for _ in range(N)]

best_cost = float('inf')
best_combi = []

def backtrack(idx, protein, fat, carbon, vita, cost, chosen):
    global best_cost, best_combi

    # 조건을 만족하면 비용 비교
    if protein >= limit[0] and fat >= limit[1] and carbon >= limit[2] and vita >= limit[3]:
        if cost < best_cost:
            best_cost = cost
            best_combi = chosen[:]
        elif cost == best_cost:
            # 사전순 비교 
            if chosen < best_combi:
                best_combi = chosen[:]
        return

    # 인덱스를 넘어가면 종료
    if idx == N:
        return

    # 현재 재료 선택
    chosen.append(idx + 1)  # 재료 번호 (1-based)
    backtrack(
        idx + 1,
        protein + food[idx][0],
        fat + food[idx][1],
        carbon + food[idx][2],
        vita + food[idx][3],
        cost + food[idx][4],
        chosen
    )
    chosen.pop()

    # 현재 재료 선택 안 함
    backtrack(idx + 1, protein, fat, carbon, vita, cost, chosen)


# 시작
backtrack(0, 0, 0, 0, 0, 0, [])

# 결과 출력
if best_cost == float('inf'):
    print(-1)
else:
    print(best_cost)
    print(*best_combi)