# Дані про студентів
students = [
    {"name": "Олег", "grades": [88, 76, 90]},
    {"name": "Марія", "grades": [95, 82, 80]},
    {"name": "Сергій", "grades": [70, 60, 65]},
    {"name": "Анастасія", "grades": [85, 90, 92]},
]

# Обробка даних
for student in students:
    total_grades = 0
    num_grades = len(student["grades"])

    for grade in student["grades"]:
        total_grades += grade

    average_grade = total_grades / num_grades
    print(f"Студент: {student['name']}, Середній бал: {average_grade:.2f}")

    if average_grade >= 75:
        print(f"{student['name']} проходить у наступний семестр.")
    else:
        print(f"{student['name']} не проходить у наступний семестр.")