lst = list(input().strip())
tmp = []
for l in lst :
    tmp.append(int(l))
def solution(lst) :
    tmp = []
    for l in lst :
        tmp.append(int(l))
    if 0 not in tmp :
        return False
    tmp.remove(0)
    if sum(tmp) % 3 != 0 :
        return False
    tmp.sort(reverse=True)
    answer = ''
    for t in tmp :
        answer += str(t)
    answer += '0'
    return answer

t = solution(lst)
if t :
    print(t)
else:
    print(-1)
