numbers = []
for _ in range(5):
    number = int(input("Введіть число: "))
    numbers.append(number)

for num in numbers:
    if num % 2 == 0:
        print(f"Число {num} є парним.")
    else:
        print(f"Число {num} є непарним.")
