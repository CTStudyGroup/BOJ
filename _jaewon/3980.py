# 백트래킹 완전탐색
# 5^11은 충분히 탐색할만함.
import sys

C = int(input())

def backtrack(matrix, player, visited, total):
    # player 번호의 선수에 대한 포지션을 정한다.
    # player 번호의 선수가 가능한 포지션은 filter(x>0) 인 것들이다.
    if(player == 11):
        return total

    avail_positions = []
    for index, value in enumerate(matrix[player]):
        if(value > 0):
            avail_positions.append(index)

    maximum = 0
    for position_index in avail_positions:
        if(visited[position_index] == 0):
            visited[position_index] = 1
            total += matrix[player][position_index]

            result = backtrack(matrix, player + 1, visited, total)
            maximum = max(maximum, result)

            visited[position_index] = 0
            total -= matrix[player][position_index]

    return maximum


for _ in range(C):
    matrix = []
    for i in range(11):
        matrix.append(list(map(int, sys.stdin.readline().strip().split())))
    
    visited = [0 for _ in range(11)]
    result = backtrack(matrix, 0, visited, 0)
    print(result)
