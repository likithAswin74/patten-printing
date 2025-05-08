n = 5
for i in range(0, n):
    for j in range(i):
        print(" ", end="")
    print("* "*n, end="")
    print()
#
# op
#
# * * * * *
#  * * * * *
#   * * * * *
#    * * * * *
#     * * * * *