# 입력 받기
T = int(input())


def swap(arr):
    for i in range(0, len(arr)//2):
        temp = arr[i]
        arr[i] = arr[len(arr)-i-1]
        arr[len(arr)-i-1] = temp
    return arr


def printAnswer(arr):
    print("[" + ','.join(arr)+"]")


for _ in range(T):
    p = input()
    n = int(input())
    arr = input()

    if(arr[1:-1] == ''):
        print("error")
        continue

    arr = arr[1:-1].split(",")
    # print(arr)

    # D 없이 R로만 이루어진 경우
    if "D" not in p:
        if(len(arr)//2):
            printAnswer(swap(arr))
        else:
            printAnswer(arr)
        continue

    # D를 기준으로 나누어진 명령어 list 생성
    p_list = []
    r_string = ""
    for elem in p:
        if elem == "D":
            if(r_string):
                p_list.append(r_string)
                r_string = ""
            p_list.append(elem)
        elif elem == "R":
            r_string += "R"

    # print(p_list)
    error = False
    for command in p_list:
        # print("command:", command)
        if command == "D":
            if not arr:
                error = True
                break
            arr = arr[1:]
        elif(len(command) % 2):
            arr = swap(arr)

    if error:
        print("error")
    else:
        printAnswer(arr)
