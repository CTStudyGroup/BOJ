N = int(input())
result = []
sen = []
for _ in range(N):
    sen.append(input())
start = 0
end = -1
check = 0
while True:
    if (start-N) == end:
        result.append(sen[start])
        check += 1
        break

    if sen[start] > sen[end]:
        result.append(sen[end])
        check += 1
        end -= 1
    elif sen[start] < sen[end]:
        result.append(sen[start])
        check += 1
        start += 1
    else:
        tmp_start = start
        tmp_end = end
        no_problem = False
        while sen[tmp_start] == sen[tmp_end]:
            tmp_start += 1
            tmp_end -= 1
            if tmp_start >= (tmp_end+N):
                no_problem = True
                break
        if no_problem:
            result.append(sen[start])
            check += 1
            start += 1
        else:
            if sen[tmp_start] > sen[tmp_end]:
                result.append(sen[end])
                check += 1
                end -= 1
            elif sen[tmp_start] < sen[tmp_end]:
                result.append(sen[start])
                check += 1
                start += 1

    if check % 80 == 0:
        result.append("\n")
        check = 0
print("".join(result))