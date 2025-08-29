N, M = map(int, input().split())

# 2^20 = 1048576
# O(2^20 * 100) 완전탐색으로 해보자
# 백트래킹

clauses = []

# 각 인덱스별 ! 연산 여부를 0-based로 저장
# ex. clauses = [[(0, 0), (1, 1)], [(1, 0), (2, 1)], [(0, 1), (2, 1)], [(2, 1), (1, 1)]]
for _ in range(M):
    a, b = map(int, input().split())
    temp = []
    if a < 0:
        temp.append((abs(a) - 1, -1))
    else:
        temp.append((a - 1, 1))
    if b < 0:
        temp.append((abs(b) - 1, -1))
    else:
        temp.append((b - 1, 1))
    clauses.append(temp)


# 현재 arr 배열로 주어진 clauses 조건을 만족할 수 있는지 여부 반환
def valid(arr):
    for clause in clauses:
        value = False
        for i, r in clause:  # 인덱스, t/f 연산
            temp = arr[i] * r
            # temp값이 1이면 true, -1이면 false
            if temp > 0:  # 해당 절 or 연산을 위해 temp가 true일 때만 value 업데이트
                value = True

        if not value:  # 해당 절이 false이면
            return False

    return True


def backtracking(i):
    if i == N:  # N개 변수에 대한 모든 경우의 수 탐색 완료
        if valid(arr):
            print(1)
            exit()
        return

    # i번째 변수가 true인 경우
    arr.append(1)
    backtracking(i + 1)
    arr.pop()

    # i번째 변수가 false인 경우
    arr.append(-1)
    backtracking(i + 1)
    arr.pop()

arr = []
backtracking(0)
print(0)  # 모든 조합 탐색에서 1을 출력하지 못한 경우, 해당 clauses 만족할 수 없음
