n = 5

for i in range(0, n):
    for j in range(i):
        print(" ", end="")

    if n-2 > i > 0:    # (or) if i > 0 and i < n-2
        for j in range(n-i):
            if j == 0 or j == n-i-1:
                print("* ", end="")
            else:
                print("  ", end="")
    else:
        for j in range(n-i):
            print("* ", end="")
    print()

#op
# * * * * *
#  *     *
#   *   *
#    * *
#     *
