import random
# =========================
# ПРОГРАМА "ТАЄМНИЙ САНТА"
# =========================

# Введення учасників
participants = []
n = int(input("Скільки учасників бере участь у Таємному Санті? "))
for _ in range(n):
    name = input("Введіть ім'я учасника: ")
    participants.append(name)

# Створення wishlist кожного учасника
wishlists = {}
for participant in participants:
    wishlist = input(f"{participant}, введіть ваші побажання через кому: ").split(",")
    wishlists[participant] = [item.strip() for item in wishlist]

# Перемішуємо список
random.shuffle(participants)

# Створюємо пари для обміну подарунками
santa_pairs = {}
for i in range(len(participants)):
    santa_pairs[participants[i]] = participants[(i + 1) % len(participants)]

# Виводимо результати жеребкування
print("\nРозподіл Таємного Санти:")
for giver, receiver in santa_pairs.items():
    print(f"{giver} дарує подарунок {receiver}. Побажання: {', '.join(wishlists[receiver])}")