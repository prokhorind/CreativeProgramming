from easygui import *

rep = True
while rep:
    number = int(enterbox('Введіть число:'))

    if number % 2 == 0:
        msgbox(f'{number} є парним числом.')
    else:
        msgbox(f'{number} є непарним числом.')

    answer = buttonbox('Ще раз?', choices=['Так', 'Ні'])
    if answer == 'Ні':
        rep = False
