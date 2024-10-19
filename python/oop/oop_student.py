class Student:
    def __init__(self, name, house, year, patronus=None):
        """
        Ініціалізує об'єкт учня
        :param name: Ім'я учня
        :param house: Факультет (наприклад, 'Gryffindor', 'Slytherin', 'Hufflepuff', 'Ravenclaw')
        :param year: Курс навчання (від 1 до 7)
        :param patronus: Патронус (якщо є)
        """
        self.name = name
        self.house = house
        self.year = year
        self.patronus = patronus

    def get_details(self):
        """
        Повертає основну інформацію про учня
        """
        details = f"Name: {self.name}, House: {self.house}, Year: {self.year}"
        if self.patronus:
            details += f", Patronus: {self.patronus}"
        return details

    def study(self):
        """
        Метод для симуляції процесу навчання
        """
        return f"{self.name} is studying spells!"

    def cast_patronus(self):
        """
        Метод для виклику патронуса
        """
        if self.patronus:
            return f"{self.name} casts a Patronus in the form of a {self.patronus}!"
        else:
            return f"{self.name} cannot cast a Patronus yet."


students= []
# Створення об'єктів класу Student
harry = Student("Harry Potter", "Gryffindor", 5, "Stag")
hermione = Student("Hermione Granger", "Gryffindor", 5)
draco = Student("Draco Malfoy", "Slytherin", 5, "Dragon")


students.append(harry)
students.append(hermione)
students.append(draco)

for st in students:
    print(st.get_details())
    print(st.cast_patronus())
    print(st.study())
    print("\n")

