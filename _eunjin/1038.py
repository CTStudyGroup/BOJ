N = int(input())

numbers = []

def backtracking(num):
    numbers.append(num)

    last = num % 10
    for i in range(last):
        backtracking(num * 10 + i)

for i in range(10):
    backtracking(i)

# print(numbers)

numbers.sort()
print(numbers[N] if N < len(numbers) else -1)
