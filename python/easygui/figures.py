from easygui import *

repeat = True
while repeat:
    figures = ['Square', 'Rectangle', 'Triangle', 'Circle']
    choice = buttonbox('Select a shape:', choices=figures)

    # Словник для виклику відповідних обчислень
    calculations = {
        'Square': lambda: float(enterbox('Enter the side length:')) ** 2,
        'Rectangle': lambda: float(enterbox('Enter the length:')) * float(enterbox('Enter the width:')),
        'Triangle': lambda: 0.5 * float(enterbox('Enter the base:')) * float(enterbox('Enter the height:')),
        'Circle': lambda: 3.14 * float(enterbox('Enter the radius:')) ** 2,
    }

    result = calculations[choice]()
    msgbox(f'The area of the {choice} is: {result}')

    repeat_prompt = buttonbox('Do you want to calculate again?', choices=['Yes', 'No'])
    if repeat_prompt == 'No':
        repeat = False
