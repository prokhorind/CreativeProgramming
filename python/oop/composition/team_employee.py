class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def __str__(self):
        return f'{self.name} - {self.position}'

class Team:
    def __init__(self, team_name):
        self.team_name = team_name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def display_employees(self):
        if not self.employees:
            print(f"No employees in team {self.team_name}.")
        else:
            print(f"Employees in team {self.team_name}:")
            for employee in self.employees:
                print(employee)

# Приклад використання
team = Team("Development Team")
employee1 = Employee("Alice", "Developer")
employee2 = Employee("Bob", "Tester")

team.add_employee(employee1)
team.add_employee(employee2)
team.display_employees()
