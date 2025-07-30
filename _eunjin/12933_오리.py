string = input()

# 주어진 문자열을 문자 하나씩 보면서 현재 오리 문자열 뒤에 붙을 수 있는지 여부 판단
# 각 오리 문자열의 마지막 문자 저장해두기

ducks = []

for s in string:
    if s == 'q':  # k로 끝나는 오리 문자열에 붙이기 or 새 오리 문자열 생성
        idx = -1
        for i in range(len(ducks)):
            if ducks[i] == 'k':
                idx = i
                break

        if idx >= 0:
            ducks[idx] = 'q'
        else:
            ducks.append('q')
    elif s == 'u':  # q로 끝나는 오리 문자열에 붙이기 or 녹음 잘못됨
        idx = -1
        for i in range(len(ducks)):
            if ducks[i] == 'q':
                idx = i
                break

        if idx >= 0:
            ducks[idx] = 'u'
        else:
            print(-1)
            exit()
    elif s == 'a':  # u로 끝나는 오리 문자열에 붙이기 or 녹음 잘못됨
        idx = -1
        for i in range(len(ducks)):
            if ducks[i] == 'u':
                idx = i
                break

        if idx >= 0:
            ducks[idx] = 'a'
        else:
            print(-1)
            exit()
    elif s == 'c':  # a로 끝나는 오리 문자열에 붙이기 or 녹음 잘못됨
        idx = -1
        for i in range(len(ducks)):
            if ducks[i] == 'a':
                idx = i
                break

        if idx >= 0:
            ducks[idx] = 'c'
        else:
            print(-1)
            exit()
    else:  # c로 끝나는 오리 문자열에 붙이기 or 녹음 잘못됨
        idx = -1
        for i in range(len(ducks)):
            if ducks[i] == 'c':
                idx = i
                break

        if idx >= 0:
            ducks[idx] = 'k'
        else:
            print(-1)
            exit()

ksum = ducks.count('k')

if len(ducks) != ksum:
    print(-1)
else:
    print(ksum)
