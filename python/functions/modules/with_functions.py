# Функція для обчислення середнього
def calculate_mean(data):
    return sum(data) / len(data)

# Функція для обчислення медіани
def calculate_median(data):
    data_sorted = sorted(data)
    if len(data_sorted) % 2 == 1:
        return data_sorted[len(data_sorted) // 2]
    else:
        return (data_sorted[len(data_sorted) // 2 - 1] + data_sorted[len(data_sorted) // 2]) / 2

# Функція для обчислення моди
def calculate_mode(data):
    count = {x: data.count(x) for x in data}
    return max(count, key=count.get)

# Функція для обчислення статистичних показників
def calculate_statistics(data):
    mean = calculate_mean(data)
    median = calculate_median(data)
    mode = calculate_mode(data)
    return mean, median, mode

def main():
    # Перший набір даних
    data1 = [10, 20, 30, 40, 50]
    mean1, median1, mode1 = calculate_statistics(data1)
    print(f"Набір 1: Середнє = {mean1}, Медіана = {median1}, Мода = {mode1}")

    # Другий набір даних
    data2 = [15, 25, 35, 45, 55]
    mean2, median2, mode2 = calculate_statistics(data2)
    print(f"Набір 2: Середнє = {mean2}, Медіана = {median2}, Мода = {mode2}")

    # Третій набір даних
    data3 = [12, 22, 32, 42, 52]
    mean3, median3, mode3 = calculate_statistics(data3)
    print(f"Набір 3: Середнє = {mean3}, Медіана = {median3}, Мода = {mode3}")


if __name__ == '__main__':
    main()