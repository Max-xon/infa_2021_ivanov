from graph import *
import math

windowSize(800, 1000)
canvasSize(600, 800)
brushColor("black")
rectangle(0, 0, 600, 800)
def knigi(a, b):
    penColor("#9F8200")
    brushColor("#9F8200")
    rectangle(200-a, 550-b, 600-a, 800-b)
    penSize(0)

    brushColor("#593315")
    rectangle(202-a, 550-b, 600-a, 565-b)
    rectangle(202-a, 630-b, 600-a, 645-b)
    rectangle(202-a, 710-b, 600-a, 725-b)
    rectangle(202-a, 785-b, 600-a, 800-b)
    brushColor("#7B001C")
    ''' красные книги 1 полка'''
    rectangle(202-a, 565-b, 217-a, 630-b)
    rectangle(350-a, 565-b, 365-a, 630-b)
    rectangle(500-a, 565-b, 515-a, 630-b)
    brushColor("#534B4F")
    ''' серые'''
    rectangle(217-a, 570-b, 232-a, 630-b)
    rectangle(287-a, 570-b, 302-a, 630-b)
    rectangle(385-a, 570-b, 400-a, 630-b)
    brushColor("yellow")
    rectangle(232-a, 585-b, 252-a, 630-b)
    rectangle(480-a, 585-b, 500-a, 630-b)
    rectangle(565-a, 585-b, 585-a, 630-b)
    brushColor("#507D2A")
    ''' зеленые книги'''
    rectangle(302-a, 585-b, 322-a, 630-b)
    rectangle(365-a, 585-b, 385-a, 630-b)
    rectangle(440-a, 585-b, 460-a, 630-b)
    rectangle(515-a, 585-b, 535-a, 630-b)
    brushColor("#922B3E")
    ''' фиолетовый'''
    rectangle(535-a, 570-b, 550-a, 630-b)
    rectangle(585-a, 570-b, 600-a, 630-b)
    brushColor("#1A153F")
    rectangle(400-a, 570-b, 415-a, 630-b)
    '''второй этаж'''
    penColor("#534B4F")
    penSize(15)
    line(210-a, 710-b, 275-a, 705-b)
    penColor("#507D2A")
    line(210-a, 695-b, 255-a, 695-b)
    penColor("#7B001C")
    line(210-a, 680-b, 275-a, 685-b)
    brushColor("yellow")
    penSize(0)
    rectangle(302-a, 665-b, 322-a, 710-b)
    rectangle(450-a, 665-b, 470-a, 710-b)
    rectangle(565-a, 665-b, 585-a, 710-b)
    brushColor("#507D2A")
    rectangle(470-a, 665-b, 490-a, 710-b)
    rectangle(520-a, 665-b, 540-a, 710-b)
    penColor("#534B4F")
    penSize(15)
    line(525-a, 705-b, 570-a, 700-b)
    penColor("#7B001C")
    penSize(20)
    line(365-a, 710-b, 420-a, 648-b)
    ''' 3 этаж'''
    penSize(0)
    brushColor("#507D2A")
    rectangle(202-a, 740-b, 222-a, 785-b)
    rectangle(515-a, 740-b, 535-a, 785-b)
    brushColor("#7B001C")
    ''' красные книги 3 полка'''
    rectangle(287-a, 725-b, 302-a, 785-b)
    rectangle(435-a, 725-b, 450-a, 785-b)
    rectangle(585-a, 725-b, 600-a, 785-b)
    brushColor("yellow")
    rectangle(267-a, 740-b, 287-a, 785-b)
    rectangle(480-a, 740-b, 500-a, 785-b)
    brushColor("#922B3E")
    rectangle(302-a, 725-b, 322-a, 785-b)
    rectangle(415-a, 725-b, 435-a, 785-b)
    brushColor("#1A153F")
    rectangle(247-a, 725-b, 267-a, 785-b)
    rectangle(450-a, 725-b, 470-a, 785-b)
    penColor("#534B4F")
    penSize(15)
    line(330-a, 788-b, 395-a, 783-b)
    penColor("yellow")
    line(330-a, 773-b, 395-a, 773-b)
    penColor("#1A153F")
    line(330-a, 758-b, 395-a, 753-b)

knigi(-100, 100)

knigi(50, -150)

knigi(400, -100)
knigi(0, 0)
knigi(100, -125)
knigi(-50, 50)
knigi(-325, 730)
'''planet'''
def ellips1(x0, y0, a, b, ang):
    x = -a
    h = 0.5
    k = -0.5
    t = math.radians(ang)
    points1 = []
    points2 = []
    while x < a:
        y = b * math.sqrt(1 - (x ** 2 / a ** 2))
        xe1 = x0 - (x*math.cos(t)-y*math.sin(t))
        xe2 = x0 + (x*math.cos(t)-y*math.sin(t))
        ye1 = y0 + (x * math.sin(t) + y * math.cos(t))
        ye2 = y0 - (x * math.sin(t) + y * math.cos(t))
        points1.append((xe1, ye1))
        points2.append((xe2,ye2))
        x += h
    polygon(points1)
    polygon(points2)
penSize(18)
penColor("white")
brushColor("white")
ellips1(400, 200, 150, 150, 60)
brushColor("black")
penColor("black")
ellips1(400, 200, 165, 125, 60)

def destination(x0, y0, x1, y1):
    return math.sqrt((x0 - x1)**2 + (y0 - y1)**2)

'x0 y0 - первый фокус'
'x0 y0 - второй фокус'
'r1 - фок расстояние меньшего фокуса'
'r1 - фок расстояние большего фокуса'
'dx, dy - смешение фокусов меньшего элипса'
def ellips2(x0, y0, x1, y1, r1, r2, dx, dy):
    trig = 0
    minx = min(x0, x1)
    maxx = max(x0, x1)
    miny = min(y0, y1)
    maxy = max(y0, y1)
    for i1 in range(minx - r2, maxx + r2, 1):
        for i2 in range(miny - r2, maxy + r2, 1):
            d1 = destination(x0, y0, i1, i2)
            d2 = destination(x1, y1, i1, i2)
            d12 = destination(x0 + dx, y0 + dy, i1, i2)
            d22 = destination(x1 + dx, y1 + dy, i1, i2)
            if d1 + d2 <= r2 and d12 + d22 >= r1:
                point(i1, i2, "grey")
                trig = 1
    if trig == 0:
        print("Элипс невозможен")
ellips2(325, 125, 525, 225, 400, 400, 10, -10)


'''perviu cosmonavt'''
brushColor("grey")
penSize(5)
penColor("grey")
ellips1(80, 465, 45, 20, 90)
'''левая нога'''
ellips1(60, 520, 40, 10, 80)
ellips1(65, 570, 20, 10, 110)
ellips1(65, 593, 15, 5, 45)

'''правая нога'''
ellips1(120, 510, 40, 10, 160)
ellips1(158, 543, 20, 10, 90)
ellips1(168, 563, 15, 5, 0)
'''pravay ruka'''
ellips1(110, 440, 12, 12, 0)
ellips1(130, 430, 8, 8, 0)
ellips1(142, 420, 7, 7, 0)
'''levay ruka'''
ellips1(50, 440, 12, 12, 0)
ellips1(30, 450, 8, 8, 0)
ellips1(18, 460, 7, 7, 0)
'''head'''
ellips1(80, 410, 26, 20, 0)
brushColor("black")
penSize(1)
oval(60, 390, 100, 420)
def cosmonavt(n, a):
    brushColor("grey")
    penSize(6/n)
    penColor("grey")
    ellips1(80+70*n, 465-35*n, 45/a, 20/a, 90)
    '''левая нога'''
    ellips1(60 + 70*n + 20 - 20/a, 520 - 35*n - (55-55/a), 40/a, 10/a, 80)
    ellips1(65 + 70*n+15-15/a, 570-35*n - (105-105/a), 20/a, 10/a, 110)
    ellips1(65+70*n+15-15/a, 593-35*n - (128-128/a), 15/a, 5/a, 45)
    '''правая нога'''
    ellips1(120+70*n-(40-40/a), 510-35*n - (45-45/a), 40/a, 10/a, 160)
    ellips1(158+70*n - (78-78/a), 543-35*n - (78-78/a), 20/a, 10/a, 90)
    ellips1(168+70*n - (88-88/a), 563-35*n - (98-98/a), 15/a, 5/a, 0)
    '''pravay ruka'''
    ellips1(110+70*n-(30-30/a), 440-35*n + (25-25/a), 12/a, 12/a, 0)
    ellips1(130+70*n-(50-50/a), 430-35*n + (35-35/a), 8/a, 8/a, 0)
    ellips1(142+70*n-(62-62/a), 420-35*n + (45-45/a), 7/a, 7/a, 0)
    '''levay ruka'''
    ellips1(50+70*n+(30-30/a), 440-35*n + (25-25/a), 12/a, 12/a, 0)
    ellips1(30+70*n+(50-50/a), 450-35*n + (15-15/a), 8/a, 8/a, 0)
    ellips1(18+70*n+(62-62/a), 460-35*n + (5-5/a), 7/a, 7/a, 0)
    '''head'''
    ellips1(80+70*n, 410-35*n + (55-55/a), 26/a, 20/a, 0)
    brushColor("black")
    penColor("black")
    ellips1(80+70*n, 410-35*n+(55-55/a), 18/a, 13/a, 0)

cosmonavt(2, 2)
cosmonavt(3, 5)



run()
