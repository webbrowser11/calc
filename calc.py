ans = None

print("welcome to a simple calculator!")
operation = input("please enter the operation (*, /, +, -): ")
num1 = int(input("please enter the first number in the equation: "))
num2 = int(input("please enter the second number in the equation: "))

try:
    if operation == "*":
        ans = num1 * num2
    elif operation == "/":
        ans = num1 / num2
    elif operation == "+":
        ans = num1 + num2
    elif operation == "-":
        ans = num1 - num2
    print(ans)
except Exception as e:
    print(f"an error occured {e}")
