from tkinter import *
window = Tk()
c = Canvas(window, width=200, height=200, bg='white')
c.pack()

c.create_rectangle(10, 10, 190, 60)

c.create_rectangle(60, 80, 140, 190,  #координати діагоналі
                   fill='yellow',     #колір заповнення
                   outline='blue',    #колір межі
                   width=3)           #ширина межі  
window.mainloop()
