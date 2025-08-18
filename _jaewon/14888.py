# N은 11까지
# 연산자 개수는 10개까지
# 전체 경우의 수를 다 돌아도 시간초과에 걸리지 않음.
import collections
import math

N = int(input())
elements = list(map(int, input().split()))

# +, -, *, //
left_operators = list(map(int, input().split()))
op_map = {0: "+", 1: "-", 2: "*", 3: "//"}

def calculate(operators_array):
    operators = operators_array[:]
    stack = collections.deque(reversed(elements))

    while len(stack) > 1:
        element1 = stack.pop()
        element2 = stack.pop()

        op = operators.pop(0)

        if(op == '+'):
            stack.append(element1 + element2)
        elif(op == '-'):
            stack.append(element1 - element2)
        elif(op == '*'):
            stack.append(element1 * element2)
        elif(op == '//'):
            if (element1 < 0 and element2 < 0):
                stack.append(math.fabs(element1) // math.fabs(element2))
            elif (element1 < 0):
                stack.append((math.fabs(element1) // element2) * -1)
            elif (element2 < 0):
                stack.append((element1 // math.fabs(element2)) * -1)
            else:
                stack.append(element1 // element2)

    result = stack.pop()
    return result

maximum = -10**9
minimum = 10**9

def backtrack(depth, operators):
    global maximum
    global minimum
    if(depth == N-1):
        result = calculate(operators)
        maximum = max(maximum, result)
        minimum = min(minimum, result)
        return

    tmp = operators[:]
    # +, -, *, //
    for index, count in enumerate(left_operators):
        if (count > 0):
            left_operators[index] -= 1
            operator = op_map[index]
            tmp.append(operator)

            backtrack(depth + 1, tmp)

            left_operators[index] += 1
            tmp.pop(-1)

backtrack(0, [])
print(int(maximum))
print(int(minimum))