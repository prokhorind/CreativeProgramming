import time
from tkinter import*
tk = Tk()
canvas = Canvas(tk, width = 400, height = 400)
canvas.pack()

canvas.create_oval(10, 10, 30, 30, fill = 'red')
canvas.create_oval(10, 30, 30, 50, fill = 'blue')

for x in range(0, 60):
    canvas.move(1, 5, 0)
    canvas.move(2, 0, 5)
    tk.update()
    time.sleep(0.05)