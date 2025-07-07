def calculator(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            return "Error: Cannot divide by zero!"
        return num1 / num2
    else:
        return "Invalid operator!"

# Example usage
print("Function Calculator")
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")

result = calculator(a, b, op)
print("Result:", result)
