def calculate(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        if b != 0:
            return a / b
        else:
            return "Cannot divide by zero"
    else:
        return "Invalid operator"

def main():
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        op = input("Enter operation (+, -, *, /): ")
        result = calculate(a, b, op)
        print("Result:", result)
    except:
        print("Invalid input")

main()
