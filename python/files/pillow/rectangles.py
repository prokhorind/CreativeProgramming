from PIL import Image, ImageDraw

#pip install pillow
#Умова: Створіть зображення розміром 400x400 пікселів із фоном білого кольору.
# Намалюйте на ньому два прямокутники різного кольору, які не перекриваються.
# Розмістіть прямокутники так, щоб один був ліворуч угорі, а інший — праворуч унизу.

# Створюємо біле зображення розміром 400x400
width, height = 400, 400
image = Image.new('RGB', (width, height), color=(255, 255, 255))

# Малюємо прямокутники
draw = ImageDraw.Draw(image)

# Перший прямокутник (синій) ліворуч угорі
draw.rectangle([50, 50, 150, 150], fill=(0, 0, 255), outline=(0, 0, 0))

# Другий прямокутник (зелений) праворуч унизу
draw.rectangle([250, 250, 350, 350], fill=(0, 255, 0), outline=(0, 0, 0))

# Зберігаємо зображення
output_path = "rectangles_image.jpg"
image.save(output_path, "JPEG")
print(f"Зображення збережено як {output_path}")
