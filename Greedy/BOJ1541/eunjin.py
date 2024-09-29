# 입력 받기
string = input()

m = string.split("-")

result = 0

if(string.find("-") < 0):
    result = sum(map(int, string.split("+")))
else:
    result += sum(map(int, m[0].split("+")))
    for elem in m[1:]:
        num = sum(map(int, elem.split("+")))
        result -= num


print(result)
