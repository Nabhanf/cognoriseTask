def add(x,y):
    return  x + y
def subtract(x, y):
   
    return  x - y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y

def multiplication(x,y):
    return  x * y

try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter the second number: "))
    operation = input("Enter the arithematic operation(+,-,*,/)?: ")
    if operation == "+":
        result = add(num1, num2)
    elif operation == "-":
        result = subtract(num1, num2)
    elif operation == "*":
        result = multiplication(num1, num2)
    elif operation == "/":
        result = divide(num1, num2)

    else:
        print("Invalid operation")     

    print(f"Result : {result}")    


except ValueError:
    print("Error:Wrong Input")
