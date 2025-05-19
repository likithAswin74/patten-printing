n = 5
a = []
for i in range(n):
    for j in range(n-i-1):
        print("- ", end="")
    lst = []
    for k in range(i+1):
        if k == i:
            print("1", end="")
            lst.append(1)
        elif k == 0:
            print("1 * ", end="")
            lst.append(1)
        else:
            temp = a[k] + a[k-1]
            print(temp, end=" * ")
            lst.append(temp)

    a = lst
    print()


# op
# - - - - 1
# - - - 1 * 1
# - - 1 * 2 * 1
# - 1 * 3 * 3 * 1
# 1 * 4 * 6 * 4 * 1
