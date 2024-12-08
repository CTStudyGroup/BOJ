# 입력 받기
N = int(input())


def recursion(n):
    if n == 3:
        return ["  *  ", " * * ", "*****"]

    stars = recursion(n//2)
    x = [" "*(n//2) + star + " "*(n//2) for star in stars]
    y = [star + " " + star for star in stars]
    return x+y


result = recursion(N)
print("\n".join(result))
