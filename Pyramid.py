n = 5  # int(input())
for i in range(0, n):
    for j in range(n-i-1):
        print(" ", end="")

    for k in range(i+1):
        print("* ", end="")
    print()

# op
#     *
#    * *
#   * * *
#  * * * *
# * * * * *