def greet():
    print("Hello, world!")

def greet_user(name):
    print(f"Hello, {name}!")

def add(a, b) -> int:
    return a + b

def greet_user_with_default_value(name="User"):
    print(f"Hello, {name}!")


greet()
greet_user("Alice")
print(add(5, 3))

greet_user_with_default_value()
greet_user_with_default_value("Bob")

