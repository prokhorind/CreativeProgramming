def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

operation = "add"
x, y = 10, 5

if operation == "add":
    result = add(x, y)
elif operation == "subtract":
    result = subtract(x, y)
elif operation == "multiply":
    result = multiply(x, y)
elif operation == "divide":
    result = divide(x, y)
else:
    result = "Invalid operation"

print(result)