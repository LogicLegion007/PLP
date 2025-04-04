def calculate():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operation = input("Enter operation (+, -, *, /): ")
    
    
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        
        if num2 == 0:
            return "Error: Division by zero is not allowed."
        result = num1 / num2

    else:
        return "Error: Invalid operation. Please use +, -, *, or /."
    return f"{num1} {operation} {num2} = {result}"

if __name__ == "__main__":
    print("Simple Calculator")
    print(calculate())