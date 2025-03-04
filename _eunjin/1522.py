string = input()

# a의 등장 횟수
a = string.count('a')

# 원형이므로 끝에 한번 더 붙여주기
string += string[0:a - 1]

mn = float('inf')

for i in range(len(string) - a + 1):
    mn = min(mn, string[i:i + a].count('b'))

print(mn)
