arr = list(input())
arr.sort()

_dict = {}
for s in arr:
    if s in _dict:
        _dict[s] += 1
    else:
        _dict[s] = 1

# print(_dict)

cnt = 0
for v in _dict.values():
    if v % 2 == 1:
        cnt += 1

if cnt > 1:  # 홀수인 문자 개수가 2개 이상이면 팰린드롬 불가
    print("I'm Sorry Hansoo")
    exit()

center = ""
half = ""

for char in sorted(_dict.keys()):
    cnt = _dict[char]

    if cnt % 2 == 1:  # 홀수개의 문자는 반드시 가운데에 1개 위치해야함
        center = char
    half += char * (cnt//2)

print(half + center + half[::-1])
