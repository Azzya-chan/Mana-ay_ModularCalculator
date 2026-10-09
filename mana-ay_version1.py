
def add_numbers(num1, num2):
    return num1 + num2

def subtract_numbers(num1, num2):
    return num1 - num2

def multiply_numbers(num1, num2):
    return num1 * num2

def divide_numbers(num1, num2):
    if num2 == 0:
        return "Cannot divide by zero."
    return num1 / num2
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Choose operation:")
print("1 - Addition")
print("2 - Subtraction")
print("3 - Multiplication")
print("4 - Division")

choice = input("Enter choice: ")

result = None

if choice == "1":
    result = add_numbers(num1, num2)
elif choice == "2":
    result = subtract_numbers(num1, num2)
elif choice == "3":
    result = multiply_numbers(num1, num2)
elif choice == "4":
    result = divide_numbers(num1, num2)
else:
    result = "Invalid operation choice."
print(f"Result: {result}")


#REFLECTION BELOW

# 1The program contains four different functions: add_numbers, subtract_numbers, multiply_numbers, and divide_numbers.

# 2Each function takes two parameters, num1 and num2, which are used to hold the numbers if passed in for the calculation.

# 3 When we call a function the two integers typed in by the user are passed into the function as arguments.

# 4 The program takes the answer returned by the function, stores it in a variable called result, and displays it to the screen.

# 5 Functions divide the code into manageable parts. This makes the program far easier to read, test, and fix, and lets you reuse the same math operations whenever you need them.
