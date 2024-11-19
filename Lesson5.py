class Vector:
    MIN_COORD = 0
    MAX_COORD = 100

    @classmethod
    def validete(cls,arg):
        return cls.MIN_COORD <= arg <= cls.MAX_COORD

    def __init__(self,x,y):
        self.x = self.y = 0
        if self.validete(x) and self.validete(y):
            self.x = x
            self.y = y
        print(self.norm2(self.x, self.y))

    def get_coord(self):
        return self.x,self.y
    @staticmethod
    def norm2(x,y):
        return x*x + y*y

v = Vector(1,20)
print(Vector.norm2(4,9))
res = Vector.get_coord(v)
print(Vector.validete(50))
print(res)


