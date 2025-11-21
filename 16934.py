N = int(input())
from collections import defaultdict, deque

usernames = []
for idx in range(N) :
    name = input().strip()
    usernames.append(name)

dic = {}
name_cnt = defaultdict(int)
prefixes = set()
for name in usernames :
    name_cnt[name] += 1
    
    #똑같은 이름이 두번 이상 나오면 뒤에 숫자 붙여서 진행
    if name_cnt[name] > 1 :
        dic[name+str(name_cnt[name])] = name
        print(name+str(name_cnt[name]))
        continue
    
    nickname = ''
    for i in range(1, len(name) + 1) :
        sub = name[:i]
        if sub not in prefixes:
            nickname = sub
            break
        
    if nickname == '' :
        print(name)
    else :
        print(nickname)
    
    for i in range(1, len(name) + 1) :
        prefixes.add(name[:i])

