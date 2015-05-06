from sympy import *

from surface import *

init_printing()

x,y,z = symbols("x y z")
surf = Surface(x,y,z,y**2-z)
print(surf.distToSurface(0,0,1))
