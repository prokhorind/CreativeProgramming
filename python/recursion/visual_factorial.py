def factorial(n, depth=0):
    indent = " " * depth  # Відступ для візуалізації рівня рекурсії
    print(f"{indent}Виклик: factorial({n})")

    if n == 1:
        print(f"{indent}Базовий випадок досягнуто: factorial(1) = 1")
        return 1
    else:
        result = n * factorial(n - 1, depth + 1)
        print(f"{indent}Результат: factorial({n}) = {n} * factorial({n-1}) = {result}")
        return result

# Виклик функції
print("Фінальний результат:", factorial(5))