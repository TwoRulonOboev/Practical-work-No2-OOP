class Rectangle:
    def __init__(self, x1, y1, x2, y2, color="black"):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.color = color

    def triangle_area(self):
        width = abs(self.x2 - self.x1)
        height = abs(self.y2 - self.y1)
        return (width * height) / 2

    def __str__(self):
        return f"Координаты: ({self.x1}, {self.y1}), ({self.x2}, {self.y2}), цвет: {self.color}, площадь треугольника: {self.triangle_area()}"
    