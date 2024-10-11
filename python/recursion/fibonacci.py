def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci_iterative(n):
    a, b = 0, 1
    for i in range(2, n):
        a, b = b, a + b
    return a + b


# 0 1 2 3 5 8
print(fibonacci(6))
#print(fibonacci_iterative(40))
