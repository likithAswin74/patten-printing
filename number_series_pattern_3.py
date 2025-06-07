n = 5
val = 0
for i in range(n):
    hold = 0
    for j in range(i+1):
        if j == 0:
            val += 1
            hold = val
            print(val, end=" ")
        else:
            hold += (n-j)
            print(hold, end=" ")
    print()

# op

# 1
# 2 6
# 3 7 10
# 4 8 11 13
# 5 9 12 14 15
