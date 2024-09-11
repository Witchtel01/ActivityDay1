import math
while True:
    try:
        n = int(input("n = "))
        if n < 0:
            print("Error: Negative input.")
            continue
        break
    except:
        print("Enter a valid integer.")

print(f"The factorial of {n} is {math.factorial(n)}")