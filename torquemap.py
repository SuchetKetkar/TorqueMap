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
xlabels = next(reader)

for i in range(len(xlabels)):
    try:
        x.append(float(xlabels[i]))
    except:
        xlabels.remove('')
#xlabels.remove(0.0)

row2 = next(reader)
for i in range(len(row2)):
    try:
        z.append(float(row2[i]))
    except:
        row.remove('')

y.extend(z[0] for i in range(len(z)-1))

z.remove(z[0])

#z = row2

x = np.array(x)
y = np.array(y)
z = np.array(z)


print(len(x))
print(len(y))
print(len(z))
#for row in reader:
    #print(row)
    #print("\n")
    #if line == 0:
        #for i in range(len(row)):
            #try:
                #x.append(float(row[i]))
            #except:
                #row.remove('')
    #else:
        #for i in range(len(row)):
            #row[i] = float(row[i])
            #if i == 0:
                #y.append(row[i])
            #else:
                #z.append(row[i])
    #line+=1

#print(x)
#print(y)
#if len(y) != len(x):
    #y = np.linspace(y[0], y[-1], num = len(x))


#plt.xticks(y,y)
#plt.xticks(z,z)

#x = np.array(x)
#y = np.array(y)
#z = np.array(z)


fig = plt.figure()
ax = fig.gca(projection='3d')

plt.xticks(x,x)
#u = np.linspace(0, 2*np.pi, 100)
#v = np.linspace(0, np.pi, 100)

#x = 10 * np.outer(np.cos(u), np.sin(v))
#y = 10 * np.outer(np.sin(u), np.sin(v))
#z = 10 * np.outer(np.ones(np.size(u)), np.cos(v))
ax.scatter3D(y, x, z, linestyle  = 'solid', color = 'blue')
ax.plot(y, x, z, linestyle  = 'solid', color = 'blue')
#ax.plot3D(y,x,z)
plt.show()
