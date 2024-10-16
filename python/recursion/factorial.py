def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(factorial(5))
print(factorial_iterative(5))