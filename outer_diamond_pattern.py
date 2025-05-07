# outer diamond pattern
n = 5

for i in range(0, n):
    for j in range(n-i-1):
        print(" ", end="")

    for k in range(i+1):
        if k == 0 or k == i:
            print("* ", end="")
        else:
            print("  ", end="")
    print()

for i in range(0, n):
    for j in range(i+1):
        print(" ", end="")

    for k in range(n-i-1):
        if k == 0 or k == n-i-2:
            print("* ", end="")
        else:
            print("  ", end="")
    print()
#
# # op
#     *
#    * *
#   *   *
#  *     *
# *       *
#  *     *
#   *   *
#    * *
#     *

