from tkinter import *
def move_oval(event):
     canvas.move(1, 5, 0)
tk = Tk()
canvas = Canvas(tk, width = 400, height = 400)
canvas.pack()
canvas.create_oval(10, 10, 30, 30, fill = 'red')
canvas.bind_all('<KeyPress-Right>', move_oval)
canvas.mainloop()