import sys
import collections
input = sys.stdin.readline

R,C = map(int, input().split())

matrix = []
for row in range(R):
    matrix.append(list(input()))

minimum = 'zzzzzzzzzzzzzzzzzzzz'

# 가로 낱말 탐색
for row in range(R):
    queue = []
    for col in range(C):
        if (matrix[row][col] == '#'):
            if (len(queue) > 1):
                minimum = min(minimum, ''.join(queue))
            queue.clear()
            continue
        
        queue.append(matrix[row][col])
    if(queue and len(queue) > 1):
        minimum = min(minimum, ''.join(queue))

# 세로 낱말 탐색
for col in range(C):
    queue = []
    for row in range(R):
        if (matrix[row][col] == '#'):
            if (len(queue) > 1):
                minimum = min(minimum, ''.join(queue))
            queue.clear()
            continue
        
        queue.append(matrix[row][col])
    if(queue and len(queue) > 1):
        minimum = min(minimum, ''.join(queue))



print(''.join(minimum))