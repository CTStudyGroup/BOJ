from sys import stdin as s
from itertools import permutations

s = open("txt/2992.txt", "r")

n = int(s.readline())
value = list(map(int, str(n).strip()))

numbers = []

for i in permutations(value):
    if i[0] >= value[0]:
        number = ''

        for j in range(len(i)):
            number += str(i[j])

        numbers.append(int(number))

numbers.sort()

for i in numbers:
    if n < i:
        print(i)
        exit()

print(0)
# 19m 23s