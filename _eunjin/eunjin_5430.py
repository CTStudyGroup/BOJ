# 입력 받기
T = int(input())


def printAnswer(arr):
    print("[" + ','.join(arr)+"]")


for _ in range(T):
    p = input()
    n = int(input())
    arr = input()

    if(arr[1:-1] == '' and "D" in p):
        print("error")
        continue

    arr = arr[1:-1].split(",")
    # print(arr)

    p_list = list(p)

    error = False
    reverse = False
    start_cnt = 0
    end_cnt = 0
    for command in p_list:
        if command == "D":
            if start_cnt+end_cnt >= n:
                error = True
                break
            if reverse:
                end_cnt += 1
            else:
                start_cnt += 1
        else:
            reverse = not reverse

    if error:
        print("error")
    else:
        result_arr = arr[start_cnt:n-end_cnt]
        #print("start_cnt:", start_cnt, ",end_cnt:", end_cnt)
        if reverse:
            printAnswer(result_arr[::-1])
        else:
            printAnswer(result_arr)
