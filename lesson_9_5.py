class Stationery:
    def __init__(self, title="..."):
        self.title = title

    def draw(self):
        print("Начало", self.title)


class Pen(Stationery):
    def draw(self):
        print("Запуск отрисовки", self.title, "ручка")


class Pencil(Stationery):
    def draw(self):
        print("Запуск отрисовки", self.title, "карандаш")


class Marker(Stationery):
    def draw(self):
        print("Запуск отрисовки", self.title, "маркер")


stat = Stationery()
stat.draw()
pen = Pen("")
pen.draw()
pencil = Pencil("")
pencil.draw()
marker = Marker("")
marker.draw()