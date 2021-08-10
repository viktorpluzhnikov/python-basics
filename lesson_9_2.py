class Road:
    def __init__(self, lenght, width):
        self._lenght = lenght
        self._width = width

    def pokr(self, a=25, b=5):
        return f"{self._lenght * self._width * a * b / 1000}"


road_1 = Road(5000, 20)
print(road_1.pokr())
