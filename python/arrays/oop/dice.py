import random


class DiceThrow:
    def __init__(self, throw_number, result):
        """
        Ініціалізує об'єкт DiceThrow для конкретного кидка кубика.
        :param throw_number: Номер кидка.
        :param result: Результат кидка кубика (число від 1 до 6).
        """
        self.throw_number = throw_number
        self.result = result

    def __str__(self):
        """
        Повертає текстове представлення результату кидка кубика.
        :return: Текстове представлення об'єкта.
        """
        return f"Кидок {self.throw_number}: {self.result}"


def count_successful_throws(dice_throws):
    """
    Рахує кількість кидків, результат яких >= 4.
    :param dice_throws: Список об'єктів DiceThrow.
    :return: Кількість кидків >= 4.
    """
    count = 0
    for throw in dice_throws:
        if throw.result >= 4:
            count += 1
    return count


def main():
    # Створюємо список об'єктів DiceThrow для 5 кидків
    dice_throws = [DiceThrow(i + 1, random.randint(1, 6)) for i in range(5)]

    # Виведення результатів кожного кидка
    print("Результати кидків кубика:")
    for throw in dice_throws:
        print(throw)

    # Рахуємо кількість кидків >= 4
    successful_throws = count_successful_throws(dice_throws)
    print(f"\nКількість кидків >= 4: {successful_throws}")


if __name__ == "__main__":
    main()
