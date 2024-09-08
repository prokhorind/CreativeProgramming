number = int(input('Скільки піц замовляєте? '))
cost = float(input('Скільки коштує одна піца? '))
total = number * cost
print('Ціна без знижки', total)
discount = total * 0.1
print('Знижка', discount)
total = total - discount
print('Ціна зі знижкою', total)
