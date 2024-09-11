# Part A

# Operations                Hand    Python
# A and B                   False   False
# A or B                    True    True
# A == B                    False   False
# (A and B) == (A or B)     False   False
# A!=B                      True    True
# A<B                       False   False
# A<=B                      False   False
# A=B                       False   Invalid


# Part B
A, B = True, False
print(A and B)
print(A or B)
print(A==B)
print((A and B) == (A or B))
print(A!=B)
print(A<B)
print(A<=B)
try:
    print(A=B)
except:
    pass


# Part C
# NEEDS FLOWCHART!!!!!!!!!!!!

temp = input("Temp: ")
pressure = input("Pressure: ")
if temp > 1000 or pressure > 20:
    print("Danger")
elif 750 < temp < 1000 and 10 < pressure < 20:
    print("Normal")
else:
    print("Warning")
# 1. :::::
# a. Normal
# b. Danger
# c. Warning
# ::::::::
# 2. Yes, because they have the same logic
