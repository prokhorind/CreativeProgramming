import random

n = 10
numbers = []
for i in range(n):
    num = random.randint(-10, 10)
    numbers.append(num)

sum_numbers = sum(numbers)

even_count = 0
odd_count = 0
multiples_of_3 = 0
for number in numbers:
    if number % 3 == 0:
        multiples_of_3 += 1

    if number % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

max_number = max(numbers)

# Виводимо результати
print(f"Сгенеровані числа: {numbers}")
print(f"Сума чисел: {sum_numbers}")
print(f"Кількість парних чисел: {even_count}")
print(f"Максимальне число: {max_number}")
print(f"Кількість чисел, кратних 3: {multiples_of_3}")
# Додати
# Кількість чисел, кратних 5
# Мінімальне число
# Кількість непарних чисел
