n = 5  # int(input())
for i in range(0, n):
    for j in range(i):
        print(" ", end="")
    for j in range(n-i):
        print("* ", end="")
    print()

# op
# * * * * *
#  * * * *
#   * * *
#    * *
#     *
