from mpl_toolkits import mplot3d
import matplotlib.pylab as plt
import numpy as np

reference_data = np.loadtxt('reference.txt')
reference_data = reference_data.T
X=reference_data[0]
Y=reference_data[1]
Z=reference_data[2]

fig = plt.figure()
ax = plt.axes(projection='3d')

plt.plot(X, Y, Z)
plt.show()