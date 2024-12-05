from easygui import*
msg = "Виберіть персонажа гри"
title = "Вибір героя"
choices = ["Птах", "Заєць", "Злюка", "Кажан"] # Список варіантів
choice = choicebox(msg, title, choices)# Присвоєння змінній choice 
if (choice == "Птах"): image = "1.gif" # вибраного елемента списку
elif (choice == "Заєць"): image = "2.gif"
elif (choice == "Кажан"): image = "3.gif"
else: image = "4.gif"
msgbox ("Ваш герой " + choice, "Ваш вибір", "OK", image)
