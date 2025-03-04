import sys

# =========================
# СТРУКТУРА ДАНИХ LIST У PYTHON
# =========================

# 1. Створення списку (List) у Python
my_list = [10, 20, 30]
print("Список:", my_list)

# 2. Доступ до елементів списку (O(1))
print("Елемент з індексом 0:", my_list[0])
print("Останній елемент:", my_list[-1])

# 3. Додавання елементів
my_list.append(40)  # O(1) амортизовано
print("Список після додавання елемента:", my_list)

# 4. Вставка елемента в середину (O(n))
my_list.insert(1, 15)  # Вставка числа 15 на індекс 1
print("Список після вставки:", my_list)

# 5. Видалення елементів
my_list.remove(20)  # Видалення за значенням (O(n))
print("Список після видалення 20:", my_list)

del my_list[2]  # Видалення за індексом (O(n))
print("Список після видалення елемента з індексом 2:", my_list)

# 6. Перебір списку (O(n))
print("Перебір елементів:")
for item in my_list:
    print(item)

# 7. Динамічний розмір списку
empty_list = []
print("Початковий розмір порожнього списку (байти):", sys.getsizeof(empty_list))

empty_list.append(1)
print("Розмір списку після додавання одного елемента:", sys.getsizeof(empty_list))

# 8. Внутрішнє представлення списку
print("Внутрішня структура списку у пам'яті:")
print("Адреси об'єктів:", [id(x) for x in my_list])
