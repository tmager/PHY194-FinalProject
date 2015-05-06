import math
import random as rand

def ellipZ(x, y, a, b):
        return math.sqrt(1 - (float)(x ** 2 /(a ** 2)) - (float)(y ** 2 /(b ** 2)))

def parabZ(x, y, a, b):
        return ((float)(x ** 2 / a ** 2) + (float)(y ** 2 / b ** 2))

def coneZ(x, y, a, b):
        return math.sqrt((float)(x ** 2 / a ** 2) + (float)(y ** 2 / b ** 2))

def randPt(type, xLow, xHigh, yLow, yHigh):
        a = (float)(xHigh - xLow) / 2
        b = (float)(yHigh - yLow) / 2
        theta = rand.random()*2*math.pi
        r = rand.random()*(
        x = 
        y = 
        if type == "ellipsoid":
                z = ellipZ(x, y, a, b)
        elif type == "paraboloid":
                z = parabZ(x, y, a, b)
        elif type == "cone":
                z = coneZ(x, y, a, b)
        return [x, y, z]

print randPt("ellipsoid", -2, 2, -2, 2)
