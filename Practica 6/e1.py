import math


class Vector:
    def __init__(self, x=0, y=0, z=0):
        self.x = int(x)
        self.y = int(y)
        self.z = int(z)

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

    def __add__(self, otro):
        return Vector(self.x + otro.x, self.y + otro.y, self.z + otro.z)

    def __sub__(self, otro):
        return Vector(self.x - otro.x, self.y - otro.y, self.z - otro.z)

    def __mul__(self, escalar):
        return Vector(self.x * escalar, self.y * escalar, self.z * escalar)

    def producto_punto(self, otro):
        return self.x * otro.x + self.y * otro.y + self.z * otro.z

    def producto_cruz(self, otro):
        x = self.y * otro.z - self.z * otro.y
        y = self.z * otro.x - self.x * otro.z
        z = self.x * otro.y - self.y * otro.x
        return Vector(x, y, z)

    def magnitud(self):
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def es_perpendicular(self, otro):
        metodos = [
            self.producto_punto(otro) == 0,
            math.isclose((self + otro).magnitud(), (self - otro).magnitud()),
            math.isclose((self - otro).magnitud(), (otro - self).magnitud()),
            math.isclose((self + otro).magnitud() ** 2, self.magnitud() ** 2 + otro.magnitud() ** 2)
        ]
        return all(metodos)

    def es_paralelo(self, otro):
        metodos = [
            self._verificar_paralelo_por_escalar(otro),
            self.producto_cruz(otro).magnitud() == 0
        ]
        return any(metodos)

    def _verificar_paralelo_por_escalar(self, otro):
        if self.magnitud() == 0 or otro.magnitud() == 0:
            return True

        if otro.x != 0:
            r = self.x / otro.x
        elif otro.y != 0:
            r = self.y / otro.y
        elif otro.z != 0:
            r = self.z / otro.z
        else:
            return True

        return (math.isclose(self.x, otro.x * r) and
                math.isclose(self.y, otro.y * r) and
                math.isclose(self.z, otro.z * r))

    def proyeccion(self, otro):
        if otro.magnitud() == 0:
            return Vector(0, 0, 0)
        factor = round(self.producto_punto(otro) / otro.magnitud() ** 2, 2)
        return otro * factor

    def componente(self, otro):
        if otro.magnitud() == 0:
            return 0.0
        return round(self.producto_punto(otro) / otro.magnitud(), 2)


def ingresar_vector(orden):
    entrada = input(f"Ingrese vector {orden} (x,y,z): ").split(',')
    return Vector(entrada[0], entrada[1], entrada[2])


def main():
    vector1 = ingresar_vector("A")
    vector2 = ingresar_vector("B")

    print(f"\nVector A: {vector1}")
    print(f"Vector B: {vector2}")

    perpendicular = vector1.es_perpendicular(vector2)
    paralelo = vector1.es_paralelo(vector2)

    print(f"\nLos vectores {'son' if perpendicular else 'no son'} perpendiculares")
    print(f"Los vectores {'son' if paralelo else 'no son'} paralelos")

    proyeccion = vector1.proyeccion(vector2)
    print(f"\nProyección: {proyeccion}")

    componente = vector1.componente(vector2)
    print(f"Componente: {componente:.2f}")

if __name__ == "__main__":
    main()