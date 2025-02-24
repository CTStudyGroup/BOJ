N = int(input())
arr = list(input() for _ in range(N))

_dict = {}
for word in arr:
    x = len(word)-1
    for char in word:
        if char in _dict:
            _dict[char] += 10**x
        else:
            _dict[char] = 10**x
        x -= 1

sorted_char = sorted(_dict.values(), reverse=True)

answer = 0
n = 9
for elem in sorted_char:
    answer += elem*n
    n -= 1
print(answer)
