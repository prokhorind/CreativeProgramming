import math


def calculate_bmi(weight, height):
    return weight / (height ** 2)


# Функція для виведення результатів та коментарів
def evaluate_bmi(name, bmi):
    rounded_bmi = math.ceil(bmi)  # Округляємо BMI в більший бік
    print(f"\n{name}: BMI = {rounded_bmi}")
    if rounded_bmi < 18.5:
        print("Недостатня вага")
    elif 18.5 <= rounded_bmi < 25:
        print("Норма")
    else:
        print("Надмірна вага")


people = {}

n = int(input("Введіть кількість людей: "))

for i in range(n):
    print(f"\nЛюдина {i + 1}:")
    name = input("Ім'я: ")
    weight = float(input("Вага (кг): "))
    height = float(input("Ріст (м): "))

    # Збереження даних у словнику
    people[name] = {
        "weight": weight,
        "height": height
    }

# Обчислення BMI та виведення результатів
for name, data in people.items():
    bmi = calculate_bmi(data["weight"], data["height"])
    evaluate_bmi(name, bmi)