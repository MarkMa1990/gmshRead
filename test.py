import gmsh
import sys


import numpy as np

gmsh.initialize(sys.argv)
gmsh.option.setNumber("General.Terminal", 1)
print(gmsh.option.getNumber("Mesh.Algorithm"))

gmsh.open("cube.msh")

model = gmsh.model

print("Nodes")
tags, coord, _ = model.mesh.getNodes(3,1)
print(tags)
print(coord)

coord2 = np.asarray(coord)
coord2 = np.reshape(coord2,(np.int32(coord2.shape[0])/3,3))

print (coord2)

gmsh.finalize()

import matplotlib.pyplot as plt


