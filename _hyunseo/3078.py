import sys
from collections import defaultdict

input = sys.stdin.readline

N, K = map(int, input().split())  # N은 반 학생, K는 성적 차이
students = defaultdict(list)
for idx in range(1, N + 1) :
    name = input()
    name_length = len(name)
    students[name_length].append(idx)

def solve(s) :
    total = 0
    i, j = 0, 1
    while j < len(s) :
        if i == j :
            j += 1
            continue
        print(f'i : {i} j : {j} s[i] : {s[i]} s[j] : {s[j]}')
        if s[j] - s[i] <= K :
            total += (j-i)
            j += 1
        else :
            i += 1
    print(f'total : {total}')
    return total


answer = 0
for name_ in students.keys() :
    answer += solve(students[name_])
    
print(answer)
