N = int(input())

def recursion(n):
    if n == 1:
        return("*")
    elif n == 2:
        return(["*****", "*", "* ***", "* * *", "* * *", "*   *", "*****"])
    else:
        before = recursion(n - 1)

        l = len(before[0]) + 4
        ret = ["*" * l]
        ret.append("*")

        for i in range(len(before)):
            if i == 0:
                ret.append("* " + before[i] + "**")
            elif i == 1:
                ret.append("* " + before[i] + " " * (len(before[0])) + "*")
            else:
                ret.append("* " + before[i] + " *")

        ret.append("* " + " " * len(before[i]) + " *")
        ret.append("*" * l)

        return ret

answer = recursion(N)

for row in answer:
    print(row)
