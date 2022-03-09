import matplotlib.pyplot as plt
data = open("Chromo.txt", "r").readlines()
con = []
res = []
sp1 = plt.subplot(111)
for i in range(len(data)):
    k = data[i].split()
    con.append(k[0])
    res.append(k[1])
sp1.plot(con, res)
plt.show()
