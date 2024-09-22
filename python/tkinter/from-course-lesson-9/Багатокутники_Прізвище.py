from tkinter import *
window = Tk()
c = Canvas(window, width=200, height=200, bg='white')
c.pack()
c.create_polygon(100, 10, 20, 90, 180, 90)
c.create_polygon(40, 110, 160, 110,
                 190, 180, 10, 180,
                 fill='orange', outline='green')
window.mainloop()
