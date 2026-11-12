class Pizza:
    def __init__(self, name, size, price):
        self.name = name
        self.size = size
        self.price = price

    def show_info(self):
        print(f"Піца: {self.name}")
        print(f"Розмір: {self.size}")
        print(f"Ціна: {self.price} грн")


class Customer:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def show_info(self):
        print(f"Клієнт: {self.name}")
        print(f"Телефон: {self.phone}")


class Order:
    def __init__(self, customer, pizza):
        self.customer = customer
        self.pizza = pizza

    def show_order(self):
        print("\\n=== ЗАМОВЛЕННЯ ===")

        self.customer.show_info()
        print()

        self.pizza.show_info()
        print("-------------------------")
        print(f"Загальна сума: {self.pizza.price} грн")
        print("Замовлення оформлено!")


# Створення об'єктів
customer = Customer("Андрій", "0991234567")
pizza = Pizza("Пепероні", "Середня", 220)

order = Order(customer, pizza)

order.show_order()