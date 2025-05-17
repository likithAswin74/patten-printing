n = 5
a = []
for i in range(0, n):
    for j in range(n - i - 1):
        print(" ", end="")
    lst = []
    for k in range(i + 1):
        if k == 0 or k == i:
            print("1 ", end="")
            lst.append(1)
        else:
            temp = a[k] + a[k - 1]
            print(temp, end=" ")
            lst.append(temp)
    print()
    a = lst

# op
#     1
#    1 1
#   1 2 1
#  1 3 3 1
# 1 4 6 4 1