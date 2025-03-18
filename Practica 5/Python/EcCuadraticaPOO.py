import math

class EcuacionCuadratica:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.discriminante = b**2 - 4 * a * c

    def resolver(self):
        if self.discriminante > 0:
            r1 = (-self.b + math.sqrt(self.discriminante)) / (2 * self.a)
            r2 = (-self.b - math.sqrt(self.discriminante)) / (2 * self.a)
            return f"La ecuación tiene dos raíces {r1:.6f} y {r2:.5f}"
        elif self.discriminante == 0:
            r1 = -self.b / (2 * self.a)
            return f"La ecuación tiene una raíz {r1:.0f}"
        else:
            return "La ecuación no tiene raíces reales"

a, b, c = map(float, input("Ingrese a, b, c: ").split())

ecuacion = EcuacionCuadratica(a, b, c)

print(ecuacion.resolver())
