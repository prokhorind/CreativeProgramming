numbers = [1, 2, 3, 4, 5, 6]

# Порожній список для збереження квадратів парних чисел
squared_even_numbers = []

# Крок 1 і 2: Прохід по кожному числу, фільтрація парних та піднесення їх до квадрата
for num in numbers:
    if num % 2 == 0:          # Перевірка, чи число парне
        squared_even_numbers.append(num ** 2)  # Додавання квадрата парного числа

print("Even=", squared_even_numbers)


# Крок 3: Обчислення суми квадратів парних чисел
sum_of_squares = 0
for square in squared_even_numbers:
    sum_of_squares += square

print("Сума квадратів парних чисел:", sum_of_squares)
