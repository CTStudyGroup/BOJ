N = int(input())
words = []

result = 0
for _ in range(N):
    new = input()
    index = 0
    length = len(words)

    flag = True #True이면 새로운 단어
    while index < length:
        compare = words[index]
        if(len(compare) != len(new)):
            index += 1
            continue
        
        candidate = []
        for i in range(len(new)):
            if(compare[0] == new[i]):
                candidate.append(i)

        #candidate에는 비교를 시작할 수 있는 알파벳의 시작 인덱스 후보들이 들어있음.
        for can in candidate:
            i = can
            j = 0
            while True:
                if(new[i] != compare[j]):
                    break

                if(i == len(new)-1):
                    i = 0
                else:
                    i += 1

                if(i == can):
                    flag = False # 똑같은 단어임
                    break
                j += 1
        index += 1
    
    if(flag):
        words.append(new)
        result += 1

print(result)




    

