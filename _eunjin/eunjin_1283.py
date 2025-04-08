N = int(input())
options = [input() for _ in range(N)]  # ['New', 'Open', 'Save', 'Save As', 'Save All']

# 각 옵션의 단어마다 첫 문자가 keys에 있는지 확인, 없으면 그 문자를 단축키로 지정
# 각 옵션마다 단축키 인덱스 저장, -1이면 단축키 없음을 의미
keys = []  # 단축키
key_idx = []  # 단축키 인덱스

for option in options:
    added = False
    l = 0
    for word in option.split():  # 단어 단위로 탐색
        if word[0].upper() in keys:
            l += len(word) + 1
        else:
            keys.append(word[0].upper())
            key_idx.append(l)
            added = True
            break

    if not added:  # 문자 단위로 탐색
        for i in range(len(option)):
            if option[i] == " ":
                continue
            elif option[i].upper() in keys:
                continue
            else:
                keys.append(option[i].upper())
                key_idx.append(i)
                added = True
                break

    if not added:  # 단축키 지정 불가
        key_idx.append(-1)

# print(keys)
# print(key_idx)

for i in range(N):
    word = ""
    if key_idx[i] == -1:
        word = options[i]
    else:
        for j in range(len(options[i])):
            if j == key_idx[i]:
                word += "[" + options[i][j] + "]"
            else:
                word += options[i][j]

    print(word)
