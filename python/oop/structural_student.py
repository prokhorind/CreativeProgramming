# Функція для створення студента
from python.oop.oop_student import students


def create_student(name, house, year, patronus=None)-> dict:
    """
    Створює словник з інформацією про учня.
    """
    return {
        "name": name,
        "house": house,
        "year": year,
        "patronus": patronus
    }

# Функція для виведення інформації про учня
def get_details(student):
    """
    Повертає основну інформацію про учня у вигляді рядка.
    """
    details = f"Name: {student['name']}, House: {student['house']}, Year: {student['year']}"
    if student['patronus']:
        details += f", Patronus: {student['patronus']}"
    return details

# Функція для симуляції навчання
def study(student):
    """
    Симулює процес навчання для студента.
    """
    return f"{student['name']} is studying spells!"

# Функція для виклику патронуса
def cast_patronus(student):
    """
    Викликає патронуса, якщо студент його має.
    """
    if student['patronus']:
        return f"{student['name']} casts a Patronus in the form of a {student['patronus']}!"
    else:
        return f"{student['name']} cannot cast a Patronus yet."

# Створення студентів
harry = create_student("Harry Potter", "Gryffindor", 5, "Stag")
hermione = create_student("Hermione Granger", "Gryffindor", 5)
draco = create_student("Draco Malfoy", "Slytherin", 5, "Dragon")

students = []
students.append(harry)
students.append(hermione)
students.append(draco)

for st in students:
    print(get_details(st))
    print(cast_patronus(st))
    print(study(st))
    print("\n")
