from sympy import *
import matplotlib as mpl

class Surface:

    def __init__(self, x, y, z, expr):
        """
        Set up the Surface and the SymPy printing stuff
        """

        self.x = x
        self.y = y
        self.z = z

        self.expr = expr
        # Solve for z -- solve() always returns a list
        self.zexpr = solve(self.expr,z)[0]

        self.x0,self.y0,self.z0 = symbols("x0 y0 z0")
        self.distSq = ((self.x - self.x0)**2 + (self.y - self.y0)**2
                         + (self.z - self.z0)**2).subs(self.z,self.zexpr)
        self.distSqDx = diff(self.distSq,self.x)
        self.distSqDy = diff(self.distSq,self.y)


    def distToSurface(self,Px,Py,Pz):
        """
        Find the minimum distance from the point specified to a point on the
        surface. Returns a tuple containing the distance and the coordinates of
        of the point(s) of closest approach, i.e.
        (dist, [(x1,y1,z1), (x2,y2,z2) ...])
        """
        # Find zero points in partial derivatives to find the minimum distance
        sols = solve([self.distSqDx.subs([(self.x0,Px),(self.y0,Py),
                                         (self.z0,Pz)]),
                     self.distSqDy.subs([(self.x0,Px),(self.y0,Py),
                                         (self.z0,Pz)])],
                    [self.x,self.y],dict=True)

        # Arbitrary large number, much larger than any maximum distance will be
        min = 10000000000
        minIdx = []

        for i in range(len(sols)):
            # TODO: this doesn't deal with surfaces z values aren't unique for
            #       a given x and y; fix that
            sols[i][self.z] = self.zexpr.subs([(self.x0,Px),(self.y0,Py),
                                               (self.z0,Pz),
                                               (self.x,sols[i][self.x]),
                                               (self.y,sols[i][self.y])])
            # Find the square of the distance to the surface (since we're only
            # comparing here, no need to do lots of square roots)
            dist = self.distSq.subs([(self.x0,Px),(self.y0,Py),
                                     (self.z0,Pz),
                                     (self.x,sols[i][self.x]),
                                     (self.y,sols[i][self.y]),
                                     (self.z,sols[i][self.z])]).evalf()
            if dist < min:
                minIdx = [i]
                min = dist
            elif dist == min:
                minIdx.append(i)

        return (sqrt(min),
                [(sol[self.x].evalf(),
                  sol[self.y].evalf(),
                  sol[self.z].evalf())
                 for sol in [sols[i] for i in minIdx]])

    def printExpr(self):
        print(self.expr)
