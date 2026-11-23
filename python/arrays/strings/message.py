class Message:
    def __init__(self, text):
        self.symbols = list(text)

    def show(self):
        print("".join(self.symbols))

    def count_spaces(self):
        count = 0

        for symbol in self.symbols:
            if symbol == " ":
                count += 1

        return count

    def remove_spaces(self):
        new_symbols = []

        for symbol in self.symbols:
            if symbol != " ":
                new_symbols.append(symbol)

        self.symbols = new_symbols


message = Message("Hello Python World")

message.show()

print("Кількість пробілів:", message.count_spaces())

message.remove_spaces()

message.show()