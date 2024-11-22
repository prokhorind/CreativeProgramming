def write_to_file(filename):
    text = input("Введіть текст для запису у файл: ")
    with open(filename, "w") as file:
        file.write(text)
    print("Текст успішно записано у файл.")


def read_from_file(filename):
    try:
        with open(filename, "r") as file:
            content = file.read()
        print("Текст з файлу:")
        print(content)
    except FileNotFoundError:
        print("Файл не знайдено!")


def main():
    filename = "example.txt"

    while True:
        print("\nМеню:")
        print("1. Запис у файл")
        print("2. Читання з файлу")
        print("3. Вихід")

        choice = input("Виберіть опцію (1, 2, 3): ")

        if choice == "1":
            write_to_file(filename)
        elif choice == "2":
            read_from_file(filename)
        elif choice == "3":
            print("До побачення!")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")


if __name__ == "__main__":
    main()
