# 백트래킹

N = int(input())
numbers = list(map(int, input().split()))

maximum = 0
length = len(numbers)

def calculate(result):
    total = 0
    for i in range(len(result)-1):
        total += abs(result[i] - result[i-1])
    return total

def backtrack(visited, depth, result):
    global maximum
    if(depth == length):
        maximum = max(maximum, calculate(result))
        return
    
    for index, number in enumerate(numbers):
        if(not visited[index]):
            result.append(number)
            visited[index] = 1
            backtrack(visited, depth + 1, result)
            visited[index] = 0
            result.pop(-1)

    return

backtrack([0 for _ in range(length)], 0, [])
print(maximum)