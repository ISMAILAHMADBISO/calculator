def calculator():
    """
    A simple calculator program that performs basic arithmetic operations.
    """
    print("Basic Calculator Program")
    
    # Get input from the user
    try:
        num1 = float(input("Enter the first number: "))
        operator = input("Enter an operator (+, -, *, /, %): ").strip()
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter numeric values for numbers.")
        return

    # Perform the operation
    if operator == '+':
        result = num1 + num2
        print(f"The result of {num1} + {num2} is {result}.")
    elif operator == '-':
        result = num1 - num2
        print(f"The result of {num1} - {num2} is {result}.")
    elif operator == '*':
        result = num1 * num2
        print(f"The result of {num1} * {num2} is {result}.")
    elif operator == '/':
        if num2 != 0:
            result = num1 / num2
            print(f"The result of {num1} / {num2} is {result}.")
        else:
            print("Error: Division by zero is not allowed.")
    elif operator == '%':
        if num2 != 0:
            result = num1 % num2
            print(f"The result of {num1} % {num2} is {result}.")
        else:
            print("Error: Modulus by zero is not allowed.")
    else:
        print("Invalid operator. Please use one of the following: +, -, *, /, %.")

# Run the calculator program
calculator()
