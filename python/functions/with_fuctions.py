
def calculate_average(grades):
    total = sum(grades)
    return total / len(grades) if grades else 0


def determine_pass(average_grade, passing_grade=75):
    return average_grade >= passing_grade


def process_students(students):
    for student in students:
        average_grade = calculate_average(student["grades"])
        print(f"Студент: {student['name']}, Середній бал: {average_grade:.2f}")

        if determine_pass(average_grade):
            print(f"{student['name']} проходить у наступний семестр.")
        else:
            print(f"{student['name']} не проходить у наступний семестр.")


if __name__ == "__main__":
    st = [
        {"name": "Олег", "grades": [88, 76, 90]},
        {"name": "Марія", "grades": [95, 82, 80]},
        {"name": "Сергій", "grades": [70, 60, 65]},
        {"name": "Анастасія", "grades": [85, 90, 92]},
    ]
    process_students(st)