class Sphere:

    def __init__(self):
        self.x = 0
        self.y = 0
        self.z = 0
        self.r = 0
        self.packed = False

    def __init__(self,x,y,surf,r):
        self.x = x
        self.y = y
        self.z = surf.eval(x,y)
        self.r = r
        self.packed = False

    def setSurface(self,surf):
        self.surf = surf

    def setRadius(self,r):
        self.r = r

    def inflate(self,factor):
        r *= factor
        
    def intersects(self,sphere2):
        return (sqrt( (sphere2.x - self.x)**2
                    + (sphere2.y - self.y)**2
                    + (sphere2.z - self.z)**2 )  < (self.r + sphere2.r))

    def adjacent(self,sphere2):
        return (sqrt( (sphere2.x - self.x)**2
                    + (sphere2.y - self.y)**2
                    + (sphere2.z - self.z)**2 )  <= (self.r + sphere2.r))

    def setPacked(self):
        self.packed = True

    def setNotPacked(self):
        self.packed = False

    def isPacked(self):
        return self.packed
