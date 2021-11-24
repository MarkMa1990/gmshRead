
import numpy as np
import matplotlib.pyplot as plt

#data = np.loadtxt("MPI_LaserInducedNPGrowth2.out", delimiter=",",skiprows=36)
data = np.loadtxt("all_vertex_2d.txt",delimiter=',')

print data.shape

print np.where(data[:,0]==np.max(data[:,0]))
print data[np.where(data[:,0]==np.max(data[:,0]))[0],0]

u, indicies = np.unique(data[:,0], return_index=True)

print u.shape
print indicies

print np.float32(data.shape[0]) / np.float32(u.shape[0])

plt.figure(0)
plt.plot(data[:,1]*1e6,data[:,2]*1e6,'b.',markersize=1)
plt.savefig("aftermesh.png")

plt.figure(1)
plt.plot(data[indicies,1]*1e6, data[indicies,2]*1e6, 'b.',markersize=1)

plt.figure(2)
plt.subplot(211)
plt.plot(data[np.argsort(data[:,0]),0])
#plt.plot(data[:,0])
plt.subplot(212)
plt.plot(indicies[np.argsort(indicies)])
#plt.plot(indicies)


plt.show()

print indicies

ind_u = data[indicies,0]
x_u = data[indicies,1]
y_u = data[indicies,2]
#z_u = data[indicies,3]

ind_u = ind_u[np.argsort(ind_u)]
x_u = x_u[np.argsort(ind_u)]
y_u = y_u[np.argsort(ind_u)]
#z_u = z_u[np.argsort(ind_u)]

print indicies

np.savetxt("indexTop.txt",np.c_[ind_u],fmt="%d")
np.savetxt("vertexTop_x_y.txt",np.c_[x_u, y_u])

plt.figure(3)
plt.plot(x_u, y_u,'b.',markersize=1)
plt.show()
