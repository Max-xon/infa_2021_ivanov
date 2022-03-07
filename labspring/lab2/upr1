
import matplotlib.pyplot as plt
sp1 = plt.subplot(111)
word = input()
con = []
res = []
plt.xlabel('Concentration, nM')
plt.ylabel('Response')
plt.grid(True, axis='y')
while word != '':
    k = word.split()
    con.append(k[0])
    res.append(k[1])
    word = input()
for i in range(len(con)):
    sp1.scatter(con[i], res[i])
plt.show()
