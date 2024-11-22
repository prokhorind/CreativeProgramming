# Перетворення тексту в ASCII коди
text = "Hello, World!"
ascii_codes = [ord(char) for char in text]

print("ASCII коди тексту:")
print(ascii_codes)

# Перетворення ASCII кодів назад у текст
reversed_text = ''.join(chr(code)  for code in ascii_codes)

print("Відновлений текст:")
print(reversed_text)
