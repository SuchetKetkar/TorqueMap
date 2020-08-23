import matplotlib.pyplot as plt
import mpl_toolkits
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import csv

filename = input("Please enter the Torque Map file name. Please ensure that it is a CSV type file.\n")

try:
    Tmap = open(filename)
except IOError:
    print("Could not open file, please select a different one")


#z is torque
# x is BV angle
# y is the RPM
x = []
y = []
z = []


reader = csv.reader(Tmap, delimiter = ",")
line = 0
for row in reader:
    print(row)
    print("\n")
    if line == 0:
        for i in range(len(row)):
            try:
                x.append(float(row[i]))
            except:
                row.remove('')
    else:
        for i in range(len(row)):
            row[i] = float(row[i])
            if i == 0:
                y.append(row[i])
            else:
                z.append(row[i])
    line+=1
print("x:    " + str(x))
print("\n")
print("y     " + str(y))
print("\n")
print("z     " + str(z))




#fig = plt.figure()
#ax = fig.gca(projection='3d')

#u = np.linspace(0, 2*np.pi, 100)
#v = np.linspace(0, np.pi, 100)

#x = 10 * np.outer(np.cos(u), np.sin(v))
#y = 10 * np.outer(np.sin(u), np.sin(v))
#z = 10 * np.outer(np.ones(np.size(u)), np.cos(v))
#ax.plot_surface(x, y, z, rstride = 4, cstride = 4, color = 'b')

#plt.show()
