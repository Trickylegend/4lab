


class Vector:
    min_cord = 0
    max_cord = 100

    @classmethod
    def validate(cls, arg):
        return cls.min_cord <= arg <= cls.max_cord

    def __init__(self, x, y):
        self.x = x
        self.y = y
        print(self.norm2(self.x, self.y))

    def get_coord(self):
        return self.x, self.y

    @staticmethod
    def norm2(x, y):
        return x * x + y * y


v = Vector(1, 2)

print(Vector.validate(5))

print(Vector.get_coord(v))

print(Vector.norm2(2, 3))