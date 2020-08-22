import matplotlib.pyplot as plt
import mpl_toolkits
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import csv

filname = input("Please enter the Torque Map file name. Please ensure that it is a CSV type file.")

try:
    Tmap = open(filename)
except IOError:
    print("Could not open file, please select a different one")

reader = csv.reader(Tmap, delimiter = ",")
for row in reader:
    print(row)

"
fig = plt.figure()
ax = fig.gca(projection='3d')

u = np.linspace(0, 2*np.pi, 100)
v = np.linspace(0, np.pi, 100)

x = 10 * np.outer(np.cos(u), np.sin(v))
y = 10 * np.outer(np.sin(u), np.sin(v))
z = 10 * np.outer(np.ones(np.size(u)), np.cos(v))
ax.plot_surface(x, y, z, rstride = 4, cstride = 4, color = 'b')

plt.show()""
