from tkinter import *
window = Tk()
c = Canvas(window, width=100, height=100, bg='white')
c.pack()
c.create_line( 10,10,   90,10)         #малювання горизонтальної лінії
c.create_line((50,20),(50,90),         #малюваамия вертикальної лінії
                fill='green',          #колір лінії
                width=3,               #товщина лінії
                arrow=FIRST,           #напрям стрілки: FIRST - вгору, LAST - донизу
                dash=(10,2),           #тип штриховки
                activefill='red',      #колір при наведенні
                arrowshape="10 25 10") #вигляд стрілки
window.mainloop()