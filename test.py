import gmsh
import sys


import numpy as np

gmsh.initialize(sys.argv)
gmsh.option.setNumber("General.Terminal", 1)
print(gmsh.option.getNumber("Mesh.Algorithm"))

gmsh.open("cube2d.msh")

model = gmsh.model

print("Nodes")
tags, coord, _ = model.mesh.getNodes(2,-1)
print(tags)
print(coord)

coord2 = np.asarray(coord)
coord2 = np.reshape(coord2,(np.int32(coord2.shape[0])/3,3))

print (coord2)

gmsh.finalize()

import matplotlib.pyplot as plt
plt.figure(0)
plt.plot(coord2[:,0],coord2[:,1],'b.')
plt.show()
