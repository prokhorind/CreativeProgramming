# Вказуємо ім'я файлу
filename = "example.txt"

# Записуємо текст у файл
with open(filename, "w") as file:
    file.write("Це приклад тексту, записаного у файл.")

# Зчитуємо текст із файлу
with open(filename, "r") as file:
    content = file.read()

# Виводимо текст у консоль
print("Текст з файлу:")
print(content)
