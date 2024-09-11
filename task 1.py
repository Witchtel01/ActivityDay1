# Part A:
# Adding 0 to the list.
# Adding 1 to the list.
# Adding 2 to the list.
# Adding 3 to the list.
# Adding 4 to the list.
# Adding 5 to the list.
# List consists of: 0
# List consists of: 1
# List consists of: 2
# List consists of: 3
# List consists of: 4
# List consists of: 5

num = 1
prevNum = 0
tempNum = 0
n = int(input("N?"))
while n>=0:
    print(prevNum)
    tempNum=num
    num +=prevNum
    prevNum=tempNum
    n-=1



num = 1
prevNum = 0
tempNum = 0
n = int(input("Max?"))
while prevNum<n:
    print(prevNum)
    tempNum=num
    num +=prevNum
    prevNum=tempNum
print(prevNum)
# For and while loops are used during iteration (used for looping)
# (For repetitive tasks)
# For loops goes for a certain number of times, while loops goes until
# the condition is false
# For loops continue until they reach the end of their specified range
# While loops terminate when the condition is false

