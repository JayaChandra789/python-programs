# Define the divide function
def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

# Take input from the user
numerator = float(input("Enter the numerator: "))
denominator = float(input("Enter the denominator: "))

# Call the divide function
result = divide(numerator, denominator)

# Print the result
print("Result:", result)
