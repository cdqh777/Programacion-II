class Figura:
    def area(self):
        raise NotImplementedError("Metodo no implementado")

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        from math import pi
        return pi * self.radio ** 2

class Rectangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

class TrianguloRec(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return ((self.base * self.altura) / 2)

class Trapecio(Figura):
    def __init__(self, baseMayor, baseMenor, altura):
        self.baseMayor = baseMayor
        self.baseMenor = baseMenor
        self.altura = altura

    def area(self):
        return ((self.baseMayor + self.baseMenor) * self.altura) / 2

class Pentagono(Figura):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        from math import tan, pi
        return(5 * self.lado ** 2) / (4 * tan(pi / 5))

def calcularArea(figura):
    return figura.area()

rectangulo = Rectangulo(5, 10)
circulo = Circulo(7)
triangulo = TrianguloRec(6, 8)
trapecio = Trapecio(10, 6, 4)
pentagono = Pentagono(5)

print("Rectangulo: ", calcularArea(rectangulo))
print("Circulo: ", calcularArea(circulo))
print("Triangulo: ", calcularArea(triangulo))
print("Trapecio: ", calcularArea(trapecio))
print("Pentagono: ", calcularArea(pentagono))

