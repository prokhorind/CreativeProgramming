# Вхідний список
numbers = [8, 3, 6, 12, 7]

# Знаходження максимального значення
max_number = max(numbers)

print("Максимальне значення у списку:", max_number)


# Ініціалізація змінної для максимального значення
max_number = numbers[0]  # Припустимо, що перший елемент - найбільший

# Цикл для знаходження максимального значення
for num in numbers:
    if num > max_number:
        max_number = num

print("Максимальне значення у списку:", max_number)