def solve(time):
    points = set()
    for start, end in time:
        points.add(start)
        points.add(end)
    points = sorted(points)
    mapping = {x: i for i, x in enumerate(points)}

    arr = [0] * (len(points) + 1)

    for start, end in time:
        arr[mapping[start]] += 1
        arr[mapping[end]] -= 1

    for i in range(1, len(points)):
        arr[i] += arr[i-1]

    return max(arr)

N = int(input())
time = [tuple(map(int, input().split())) for _ in range(N)]
print(solve(time))