from tkinter import *
from random import randrange as rnd, choice
import time

root = Tk()
root.geometry('800x600')

canv = Canvas(root, bg='white')
canv.pack(fill=BOTH, expand=1)

colors = ['red', 'orange', 'yellow', 'green', 'blue']
count = 0
def new_ball():
    global x,y,r
    canv.delete(ALL)
    x = rnd(100,700)
    y = rnd(100,500)
    r = rnd(30,50)
    canv.create_oval(x-r, y-r, x+r, y+r, fill=choice(colors), width=0)

    root.after(1000, new_ball)


def click(event):
    global count

    if ((x - event.x)**2 + (y - event.y)**2)**(1/2) < r:
        count += 1
        canv.delete(ALL)

    print(count)
    print(x,y,r, end="\n")

new_ball()
canv.bind('<Button-1>', click)
mainloop()