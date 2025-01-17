N = int(input())


def recursion(n):
    # base case
    if n == 3:
        return ["  *  ", " * * ", "*****"]

    # recursive case
    stars = recursion(n//2)
    first = []
    second = []
    for star in stars:
        first.append(" "*(n//2)+star+" "*(n//2))
        second.append(star+" "+star)
    return first+second


print('\n'.join(recursion(N)))
