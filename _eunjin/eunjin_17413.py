# 입력 받기
S = list(input())

result = []
temp = []

while S:
    char = S.pop(0)

    if char == "<":
        while temp:
            word = temp.pop()
            result.append(word)

        result.append(char)
        while S:
            char = S.pop(0)
            result.append(char)
            if(char == ">"):
                break
        continue
    if char == " ":
        while temp:
            word = temp.pop()
            result.append(word)
        result.append(char)
        continue
    temp.append(char)

while temp:
    char = temp.pop()
    result.append(char)


print(''.join(result))
