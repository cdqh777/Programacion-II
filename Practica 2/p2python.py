import math

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def coord_cartesianas(self):
        return (self.x, self.y)

    def coord_polares(self):
        r = math.sqrt(self.x**2 + self.y**2)
        theta = math.atan2(self.y, self.x)
        return (r, theta)

    def __str__(self):
        return f"Punto(x={self.x}, y={self.y})"

class Linea:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __str__(self):
        return f"Linea(p1={self.p1}, p2={self.p2})"

    def dibujalinea(self):
        print(f"Dibujando línea desde {self.p1} hasta {self.p2}")

class Circulo:
    def __init__(self, centro, radio):
        self.centro = centro
        self.radio = radio

    def __str__(self):
        return f"Circulo(centro={self.centro}, radio={self.radio})"

    def dibujacirculo(self):
        print(f"Dibujando círculo con centro en {self.centro} y radio {self.radio}")

p1 = Punto(1, 2)
p2 = Punto(3, 4)
linea = Linea(p1, p2)
print(linea)
linea.dibujalinea()

centro = Punto(0, 0)
circulo = Circulo(centro, 5)
print(circulo)
circulo.dibujacirculo()