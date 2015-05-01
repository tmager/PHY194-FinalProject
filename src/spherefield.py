from sphere import *

class SphereField:

    def __init__(self,surf):
        self.spheres = []
        self.surf = surf

    def insertSphere(self,sphere):
        # Single sphere is being inserted
        if type(sphere) == Sphere:
            self.spheres.append(sphere)
        # Multiple spheres are being inserted, so 'sphere' is actually a list
        else:
            self.spheres.extend(sphere)

    def removeSphere(self,sphere):
        self.spheres.remove(sphere)

    def __len__(self):
        return len(self.spheres)

    def __getitem__(self,idx):
        return self.spheres[idx]

    def __getitem__(self,idx,value):
        self.spheres[idx] = value

    def inflate(self, factor):
        pass
