class Staionery():
    title = ""

    def draw():
        print("Запуск отрисовки")


class Pen(Staionery):

    def draw(self):
        print("Отрисовка ручкой")


class Pencil(Staionery):

    def draw(self):
        print("Отрисовка карандашем")


class Handle(Staionery):
    def draw(self):
        print("Отрисовка ручками")


pt = Staionery()
pt1 = Pen()
pt2 = Pencil()
pt3 = Handle()

Pen.draw(pt3)
Pencil.draw(pt1)
Handle.draw(pt2)
