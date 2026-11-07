print("===== SIMPLE CALCULATOR =====")

# input from the user
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

# Perform arithmetic operations
total = a + b
difference = a - b
product = a * b
print("\n===== RESULTS =====")
print("Addition  :", total)
print("Subtraction  :", difference)
print("Multiplication :", product)

# Check division by zero
if b != 0:
    division = a / b
    print("Division  :", division)
else:
    print("Division  : Cannot divide by zero")
