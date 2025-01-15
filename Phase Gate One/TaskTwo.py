try:
    num1 = int(input("Enter first number: "))
except ValueError:
    print("Invalid input. Please enter an integer.")
   
try:
    num2 = int(input("Enter second number: "))
except ValueError:
    print("Invalid input. Please enter an integer.")

try:
    num3 = int(input("Enter third number: "))
except ValueError:
    print("Invalid input. Please enter an integer.")
    

ascending_numbers = sorted([num1, num2, num3])
print(ascending_numbers)
