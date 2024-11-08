from functools import reduce

numbers = [1, 2, 3, 4, 5, 6]

# Крок 1: Фільтрація парних чисел
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even=", even_numbers)

# Крок 2: Піднесення парних чисел до квадрата
squared_even_numbers = list(map(lambda x: x ** 2, even_numbers))
print("Squared=", squared_even_numbers)

# Крок 3: Обчислення суми квадратів парних чисел
sum_of_squares = reduce(lambda x, y: x + y, squared_even_numbers)

print("Сума квадратів парних чисел:", sum_of_squares)
