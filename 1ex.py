class Square:
    def find_per(self, side):
        self.per = side * 4
        print("Периметр = ", self.per)

    def find_sq(self, side):
        self.sq = side * side
        print("Площадь = ", self.sq)

    def find_diag(self, side):
        self.diag = 2 ** (0.5) * side
        print("Диагональ = ", self.diag)


obj = Square()
obj.find_per(5)
obj.find_sq(4)
obj.find_diag(3)