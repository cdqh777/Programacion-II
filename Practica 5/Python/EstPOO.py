import math

class Estadisticas:
    def __init__(self, datos):
        self.datos = datos
        self.prom = self.promedio()
        self.desv = self.desviacion()

    def promedio(self):
        return sum(self.datos) / len(self.datos)

    def desviacion(self):
        varianza = sum((x - self.prom) ** 2 for x in self.datos) / (len(self.datos) - 1)
        return math.sqrt(varianza)

datos = list(map(float, input().split()))
estadisticas = Estadisticas(datos)

print(f"El promedio es {estadisticas.prom:.2f}")
print(f"La desviación estándar es {estadisticas.desv:.5f}")
