# Part A
# Using standard x-y axis (x horizontal, y vertical)
# 12:   (0, 20)
# 1:    (10, 17.32051)
# 2:    (17.32051, 10)
# 3:    (20, 0)
# 4:    (17.32051, -10)
# 5:    (10, -17.32051)
# 6:    (0, -20)
# 7:    (-10, -17.32051)
# 8:    (-17.32051, -10)
# 9:    (-20, 0)
# 10:   (-17.32051, 10)
# 11:   (-10, 17.32051)




# Part B
x = input("X = ")
y = input("Y = ")
if x == 0:
    if y == 20:
        print("12:00 ring 12")
    else:
        print("6:00 ring 6")
elif x == 10:
    if y == 17.32051:
        print("1:00 ring 1")
    else:
        print("5:00 ring 5")
elif x == -10:
    if y == 17.32051:
        print("11:00 ring 11")
    else:
        print("7:00 ring 7")
elif x == 17.32051:
    if y == 10:
        print("2:00 ring 2")
    else:
        print("4:00 ring 4")
elif x == -17.32051:
    if y == 10:
        print("10:00 ring 10")
    else:
        print("8:00 ring 8")
else:
    if x == 20:
        print("3:00 ring 3")
    else:
        print("9:00 ring 9")




# Part C
x = input("X = ")
y = input("Y = ")
if x == 0:
    if y == 20:
        print("12:30 ring 1")
    else:
        print("6:30 ring 1")
elif x == 10:
    if y == 17.32051:
        print("1:30 ring 1")
    else:
        print("5:30 ring 1")
elif x == -10:
    if y == 17.32051:
        print("11:30 ring 1")
    else:
        print("7:30 ring 1")
elif x == 17.32051:
    if y == 10:
        print("2:30 ring 1")
    else:
        print("4:30 ring 1")
elif x == -17.32051:
    if y == 10:
        print("10:30 ring 1")
    else:
        print("8:30 ring 1")
else:
    if x == 20:
        print("3:30 ring 1")
    else:
        print("9:30 ring 1")



# Part D
x = float(input("X = "))
y = float(input("Y = "))
half = bool(input("Half? (True or False) "))
if half is False:
    x = input("X = ")
    y = input("Y = ")
    if x == 0:
        if y == 20:
            print("12:00 ring 12")
        else:
            print("6:00 ring 6")
    elif x == 10:
        if y == 17.32051:
            print("1:00 ring 1")
        else:
            print("5:00 ring 5")
    elif x == -10:
        if y == 17.32051:
            print("11:00 ring 11")
        else:
            print("7:00 ring 7")
    elif x == 17.32051:
        if y == 10:
            print("2:00 ring 2")
        else:
            print("4:00 ring 4")
    elif x == -17.32051:
        if y == 10:
            print("10:00 ring 10")
        else:
            print("8:00 ring 8")
    else:
        if x == 20:
            print("3:00 ring 3")
        else:
            print("9:00 ring 9")
else:
    if x == 0:
        if y == 20:
            print("12:30 ring 1")
        else:
            print("6:30 ring 1")
    elif x == 10:
        if y == 17.32051:
            print("1:30 ring 1")
        else:
            print("5:30 ring 1")
    elif x == -10:
        if y == 17.32051:
            print("11:30 ring 1")
        else:
            print("7:30 ring 1")
    elif x == 17.32051:
        if y == 10:
            print("2:30 ring 1")
        else:
            print("4:30 ring 1")
    elif x == -17.32051:
        if y == 10:
            print("10:30 ring 1")
        else:
            print("8:30 ring 1")
    else:
        if x == 20:
            print("3:30 ring 1")
        else:
            print("9:30 ring 1")