import math


def calculate_bmi(weight, height):
    return weight / (height ** 2)


def evaluate_bmi(name, bmi):
    rounded_bmi = math.ceil(bmi)
    print(f"\n{name}: BMI = {rounded_bmi}")
    if rounded_bmi < 18.5:
        print("Недостатня вага")
    elif 18.5 <= rounded_bmi < 25:
        print("Норма")
    else:
        print("Надмірна вага")

def print_bmi(people: dict):
    # Обчислення BMI та виведення результатів
    for name, data in people.items():
        bmi = calculate_bmi(data["weight"], data["height"])
        evaluate_bmi(name, bmi)

def save_input(peoplenum) -> dict:
    people = {}
    for i in range(peoplenum):
        print(f"\nЛюдина {i + 1}:")
        name = input("Ім'я: ")
        weight = float(input("Вага (кг): "))
        height = float(input("Ріст (м): "))

        people[name] = {
            "weight": weight,
            "height": height

        }
    return people


if __name__ == "__main__":
    n = int(input("Введіть кількість людей: "))
    people_input = save_input(n)
    print_bmi(people_input)