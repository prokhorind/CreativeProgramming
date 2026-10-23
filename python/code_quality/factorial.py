def calculate_factorial(number: int) -> int:
    """
    Обчислює факторіал заданого цілого невід'ємного числа.
    
    Аргументи:
        number (int): Число, для якого потрібно обчислити факторіал.
        
    Повертає:
        int: Значення факторіала числа.
    """
    # 1. Перевірка на коректність: факторіал від'ємного числа не визначено
    if number < 0:
        raise ValueError("Факторіал від'ємного числа не визначено.")
    
    # 2. Базовий випадок: факторіал 0 та 1 дорівнює 1
    if number == 0 or number == 1:
        return 1
        
    # 3. Ініціалізація змінної для збереження проміжного та кінцевого результату
    factorial_result = 1
    
    # 4. Цикл для послідовного множення чисел від 2 до заданого числа включно
    for current_number in range(2, number + 1):
        factorial_result *= current_number
        
    return factorial_result


if __name__ == "__main__":
    # 5. Приклад використання функції та виведення результату
    target_number = 5
    result = calculate_factorial(target_number)
    print(f"Факторіал числа {target_number} дорівнює {result}")
