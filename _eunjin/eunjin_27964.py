N = int(input())
arr = list(input().split())

cheese = set()

for topping in arr:
    if len(topping) >= 6 and topping[-6:] == "Cheese":
        cheese.add(topping)

# print(cheese)

if len(cheese) >= 4:
    print("yummy")
else:
    print("sad")
