n = 5  # int(input())
for i in range(0, n):
    for j in range(n-i-1):
        print(" ", end="")

    if i == n - 1:
        print("* " * n, end="")
    else:
        for k in range(i+1):
            if k == 0 or k == i:
                print("* ", end="")
            else:
                print("  ", end="")
    print()


#         (or)

# for i in range(0, n):
#
#     for j in range(n-i-1):
#         print(" ", end="")
#
#     if 1 < i < n - 1:  # or if i > 1 and i < n-1:
#         for k in range(i+1):
#             if k == 0 or k == i:
#                 print("* ", end="")
#             else:
#                 print("  ", end="")
#     else:
#         for k in range(i+1):
#             print("* ", end="")
#     print()

#op
#     *
#    * *
#   *   *
#  *     *
# * * * * *