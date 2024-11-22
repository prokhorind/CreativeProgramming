# Приклад 1: Отримання символу за індексом
string = "Python"
print("Перший символ:", string[0])  # Виведе 'P'
print("Останній символ:", string[-1])  # Виведе 'n'

print("-" * 30)

# Приклад 2: Ітерація по символах рядка
string = "Привіт"
print("Символи в рядку:")
for char in string:
    print(char)
# Виведе кожен символ: 'П', 'р', 'и', 'в', 'і', 'т'

print("-" * 30)

# Приклад 3: Заміна символа в рядку
string = "hello"
index_to_replace = 1
new_char = 'a'

new_string = string[:index_to_replace] + new_char + string[index_to_replace + 1:]
print("Після заміни символа:", new_string)  # Виведе 'hallo'

print("-" * 30)

# Приклад 4: Пошук індексу певного символа
string = "abcdefg"
target = 'd'

if target in string:
    print(f"Символ '{target}' знайдено на індексі:", string.index(target))  # Виведе 3
else:
    print(f"Символ '{target}' не знайдено.")

print("-" * 30)

# Приклад 5: Перевертання рядка
string = "Python"
reversed_string = string[::-1]
print("Перевернутий рядок:", reversed_string)  # Виведе 'nohtyP'
