class BankAccount:
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        return f"{self.owner} поповнив рахунок на {amount} грн. Баланс: {self.balance} грн"

    def withdraw(self, amount):
        if amount > self.balance:
            return f"Недостатньо коштів на рахунку. Баланс: {self.balance} грн"
        self.balance -= amount
        return f"{self.owner} зняв {amount} грн. Баланс: {self.balance} грн"

    def check_balance(self):
        return f"Баланс: {self.balance} грн"


# Приклад використання
account = BankAccount("Іван Іванов")
print(account.deposit(1000))  # Іван Іванов поповнив рахунок на 1000 грн. Баланс: 1000 грн
print(account.withdraw(300))  # Іван Іванов зняв 300 грн. Баланс: 700 грн
print(account.check_balance())  # Баланс: 700 грн

account2 = BankAccount("John Smith")
print(account2.deposit(2000))  # John Smith поповнив рахунок на 2000 грн. Баланс: 2000 грн
print(account2.withdraw(500))  # John Smith зняв 500 грн. Баланс: 1500 грн
print(account2.check_balance())  # Баланс: 1500 грн
