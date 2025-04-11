n = 5 # int(input())

for i in range(1, n+1):
    print("*"*i)

# (or)

for i in range(0, n):
    for j in range(i+1):
        print("*", end="")
    print()