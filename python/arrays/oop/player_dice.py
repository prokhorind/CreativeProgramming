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


class Player:
    def __init__(self, name):
        """
        Ініціалізує об'єкт гравця.
        :param name: Ім'я гравця.
        """
        self.name = name
        self.throws = []

    def throw_dice(self):
        """
        Кидає кубик 5 разів і зберігає результати.
        """
        self.throws = [DiceThrow(i + 1, random.randint(1, 6)) for i in range(5)]

    def __str__(self):
        """
        Повертає текстове представлення результатів кидків для цього гравця.
        :return: Текстове представлення результатів кидків.
        """
        return f"Гравець {self.name}:\n" + "\n".join(str(throw) for throw in self.throws)


def count_wins(player1, player2):
    """
    Рахує кількість перемог кожного гравця.
    :param player1: Об'єкт гравця 1.
    :param player2: Об'єкт гравця 2.
    :return: Кількість перемог для кожного гравця.
    """
    player1_wins = 0
    player2_wins = 0

    for throw1, throw2 in zip(player1.throws, player2.throws):
        if throw1.result > throw2.result:
            player1_wins += 1
        elif throw1.result < throw2.result:
            player2_wins += 1

    return player1_wins, player2_wins


def main():
    # Створюємо двох гравців
    player1 = Player("Гравець 1")
    player2 = Player("Гравець 2")

    # Кожен гравець кидає кубик 5 разів
    player1.throw_dice()
    player2.throw_dice()

    # Виведення результатів кидків для кожного гравця
    print(player1)
    print("\n")
    print(player2)
    print("\n")

    # Рахуємо перемоги кожного гравця
    player1_wins, player2_wins = count_wins(player1, player2)

    # Виводимо кількість перемог
    print(f"Перемоги {player1.name}: {player1_wins}")
    print(f"Перемоги {player2.name}: {player2_wins}")


if __name__ == "__main__":
    main()
