def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

# Define a dictionary to map operations to their corresponding functions
operations = {
    "add": add,
    "subtract": subtract,
    "multiply": multiply,
    "divide": divide
}

operation = "add"
x, y = 10, 5
operation_func = operations.get(operation, lambda x, y: "Invalid operation")
result = operation_func(x, y)

print(result)
