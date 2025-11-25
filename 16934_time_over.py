N = int(input())
from collections import defaultdict, deque

usernames = []
for _ in range(N) :
    usernames.append(input().strip())
    
dic = {}
name_cnt = defaultdict(int)
name_lst = defaultdict(list)

for name in usernames :
    name_cnt[name] += 1
    name_lst[name[0]].append(name)
    
    #똑같은 이름이 두번 이상 나오면 뒤에 숫자 붙여서 진행
    if name_cnt[name] > 1 :
        dic[name+str(name_cnt[name])] = name
        continue
    
    
    # 앞이 같은 이름이 없는 경우
    if len(name_lst[name[0]] )== 1 :
        dic[name[0]] = name
        continue
    
    name_set = set(name_lst[name[0]])
    name_set.remove(name)
    i = 0 
    while name_set and  i < len(name):

        name_set = {n for n in name_set if len(n) >= i+1 and n[i] == name[i]}
        i += 1
    
    answer = name[:i]
    dic[name[:i]] = name
    print(answer)

