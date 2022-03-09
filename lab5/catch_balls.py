import tkinter as tk
from tkinter import *
from random import randrange as rnd, choice
import time
from tkinter import messagebox


root = Tk()  # главное окно - объект класса ТК

root.geometry('800x900')
canv = Canvas(root, bg='white')
canv.pack(fill=BOTH, expand=1)
colors = ['red', 'green', 'yellow', 'blue']
bombs = (True, False)

l = Label(root, bg='blue', fg='white', width=20)

l.pack()

# Окошко для ввода имени пользователя

usernameLabel = Label(root, bg='white', width=50)
usernameLabel.pack()

usernameEntry = Entry(root, width=50)
usernameEntry.pack()

t = ''


def to_label(event):
    '''
    Функция считывает имя пользователя и помещает его на отдельный label
    '''
    global t
    t = usernameEntry.get()
    usernameLabel.configure(text=t)
    usernameEntry.destroy()


usernameEntry.bind('<Return>', to_label)


def new_ball():
    '''
    рисуем случайное кол-во шаров, случайного цвета и радиуса 
    balls - массив созданных шариков, которые будут перемещаться
    Бомба - шарик, обнуляющий счёт
    bombs_coords - массив с координатами бомб
    balls - массив со всеми шариками
    '''
    canv.delete(ALL)
    global x, y, r, color, balls, n, bombs_coords, bombs, rad
    n = rnd(1, 10)
    balls = []
    bombs_coords = []
    rad = []
    for i in range(n):
        x = rnd(100, 700)
        y = rnd(100, 500)
        r = rnd(30, 50)
        bomb = choice(bombs)
        rad.append(r)
        if bomb == True:
            color = 'black'
            ball = canv.create_oval(x - r, y - r, x + r, y + r, fill=color, width=0)
            bombs_coords.append(ball)
            balls.append(ball)
        else:
            color = choice(colors)
            ball = canv.create_oval(x - r, y - r, x + r, y + r, fill=color, width=0)
            balls.append(ball)
    move_ball()
    canv.after(5000, new_ball)


def move_ball():
    '''
    перемещение xspped по оси х, yspeed - перемещение по оси y
    массив balls содержит все шарики, которые создала функция new_ball
    '''
    global xspeed, yspeed, balls, n
    i = 0
    while i < n:
        xspeed = rnd(-10, 10)
        yspeed = rnd(-10, 10)
        if canv.coords(balls[i])[2] > 800:
            xspeed = rnd(-10, -1)
        if canv.coords(balls[i])[0] < 50:
            xspeed = rnd(1, 10)
        if canv.coords(balls[i])[1] < 50:
            yspeed = rnd(1, 10)
        if canv.coords(balls[i])[3] > 700:
            yspeed = rnd(-10, -1)
        canv.move(balls[i], xspeed, yspeed)
        i += 1
    canv.after(100, move_ball)


new_ball()

score = 0

'''Функция осуществляет подсчёт очков 'score'. Очко начислется, если касание мышью экрана находилось внутри шарика
    event '''
def click(event):

    global score, bombs_coords, n, rad
    for i in range(n):
        if ((event.x - canv.coords(balls[i])[0] - rad[i]) ** 2 + (event.y - canv.coords(balls[i])[1] - rad[i]) ** 2) <= \
                rad[i] ** 2:
            if balls[i] in bombs_coords:
                score = 0
            else:
                score += 1
    l['text'] = str(score)


canv.bind('<Button-1>', click)

root.mainloop()

'''Запись результатов в файл'''

string = t + ' ' + str(score) + '\n'
with open('results.txt', 'a') as f:
    f.write(string)
