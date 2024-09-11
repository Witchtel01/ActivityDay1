# Part B:::::::::::::::::::::::::::::
# NEED TO MAKE A FLOWCHART FOR PART B
# :::::::::::::::::::::::::::::::::::

# Part C
from Factorial import myFactorial
userInput = input("Please enter the numbers to be evaluated:\n")
userInput = [int(_) for _ in userInput.strip().split()]
computed = list(map(myFactorial,userInput))
for i in range(len(userInput)):
    try:
        print(f"The factorial of {userInput[i]} is {int(computed[i])}")
    except:
        print(computed[i])