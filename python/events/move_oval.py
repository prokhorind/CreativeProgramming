from tkinter import*

tk = Tk()
canvas = Canvas(tk, width = 400, height = 400)

def move_oval(event):
    if event.keysym == 'Up': canvas.move(1, 0, -3)
    elif event.keysym == 'Down': canvas.move(1, 0, 3)
    elif event.keysym == 'Left': canvas.move(1, -3, 0)
    else: canvas.move(1, 3, 0)


def init_oval():
    canvas.create_oval(10, 10, 30, 30, fill = 'red')
    canvas.bind_all('<KeyPress-Up>', move_oval)
    canvas.bind_all('<KeyPress-Down>', move_oval)
    canvas.bind_all('<KeyPress-Left>', move_oval)
    canvas.bind_all('<KeyPress-Right>', move_oval)

if __name__ == "__main__":
    canvas.pack()
    init_oval()
    canvas.mainloop()

