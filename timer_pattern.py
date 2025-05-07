# timer_pattern

n = 5
for i in range(0, n):
    for j in range(i):
        print(" ", end="")
    for j in range(n-i):
        print("* ", end="")
    print()

n = n-1 # to reduce 1 iteration
for i in range(0, n):
    for j in range(n-i-1):
        print(" ", end="")
    for k in range(i+2):
        print("* ", end="")
    print()

# op
# * * * * *
#  * * * *
#   * * *
#    * *
#     *
#    * *
#   * * *
#  * * * *
# * * * * *