import tkinter as tk
from tkinter import PhotoImage


def show_label(color_name):
    """Показує текст з назвою об'єкта англійською."""
    label.config(text=color_name, fg="black")


# Створення головного вікна
root = tk.Tk()
root.title("Кольорові квадрати")
root.geometry("1000x500")

# Мітка для виводу тексту
label = tk.Label(root, text="", font=("Arial", 16))
label.pack(pady=20)

# Словник кольорів і відповідних назв
colors = {
    "red": ("Apple", "apple.png"),
    "blue": ("Cloud", "cloud.png")
}

# Список для збереження об'єктів PhotoImage
frames = []

# Створення Canvas для прямокутників та зображень
canvas = tk.Canvas(root, width=1000, height=400)
canvas.pack()

# Розташування елементів на Canvas
x_start = 80  # Початкова координата X для прямокутників

for color, (name, img_path) in colors.items():
    # Завантаження зображення та додавання до списку frames
    img = PhotoImage(file=img_path)
    frames.append(img)

    # Додавання зображення на Canvas
    picture = canvas.create_image(x_start + 40, 300, image=frames[-1])  # frames[-1] — останній доданий елемент

    # Малювання прямокутника
    rect = canvas.create_rectangle(x_start, 50, x_start + 80, 130, fill=color, outline="black")

    # Прив'язка кліку до прямокутника
    canvas.tag_bind(rect, "<Button-1>", lambda event, name=name: show_label(name))

    # Зсув координати для наступного прямокутника
    x_start += 300

# Запуск основного циклу
root.mainloop()
