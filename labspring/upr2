a = list()
word = input()
while word != '':
    a.append(int(word))
    word = input()
a.sort()
print(a)
sum = 0
for i in range(len(a)):
    sum += a[i]
s = sum/len(a)
sr = 0
for i in range(len(a)):
    sr += (a[i] - s)**2
srpr = sr/(len(a) - 1)
print('Средне квадратичное отклонение = ', srpr**(1/2))
if len(a) % 2 == 0:
    if (len(a)/2) % 2 == 0:
        b = (a[len(a)//4-1]+a[len(a)//4])/2
        k = (a[(3*len(a))//4-1]+a[(3*len(a))//4])/2
    else:
        b = (a[len(a) // 4])
        k = (a[(3*len(a)) // 4])
else:
    if (len(a)//2 - 1) % 2 == 0:
        b = (a[len(a) // 4 - 1] + a[len(a) // 4]) / 2
        k = (a[(3 * len(a)) // 4] + a[(3 * len(a)) // 4 + 1]) / 2
    else:
        b = (a[len(a) // 4])
        k = (a[(3*len(a)) // 4])

print('Размах=', float(k-b))
