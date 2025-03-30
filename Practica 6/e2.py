import math

class VectorTridimensional:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, otro):
        return VectorTridimensional(self.x + otro.x, self.y + otro.y, self.z + otro.z)

    def __mul__(self, escalar):
        return VectorTridimensional(self.x * escalar, self.y * escalar, self.z * escalar)

    def __rmul__(self, escalar):
        return self.__mul__(escalar)

    def __matmul__(self, otro):
        return self.x * otro.x + self.y * otro.y + self.z * otro.z

    def __xor__(self, otro):
        nuevo_x = self.y * otro.z - self.z * otro.y
        nuevo_y = self.z * otro.x - self.x * otro.z
        nuevo_z = self.x * otro.y - self.y * otro.x
        return VectorTridimensional(nuevo_x, nuevo_y, nuevo_z)

    def longitud(self):
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def normalizar(self):
        magnitud = self.longitud()
        if magnitud == 0:
            return VectorTridimensional(0, 0, 0)
        return VectorTridimensional(round(self.x / magnitud, 4), round(self.y / magnitud, 4), round(self.z / magnitud, 4))

    def proyeccion_ortogonal(self, otro):
        producto_punto = self @ otro
        magnitud_cuadrado = otro @ otro
        if magnitud_cuadrado == 0:
            return VectorTridimensional(0, 0, 0)
        factor = producto_punto / magnitud_cuadrado
        proyeccion = otro * factor
        return VectorTridimensional(round(proyeccion.x, 4), round(proyeccion.y, 4), round(proyeccion.z, 4))

    def __str__(self):
        # Mostrar sin decimales si son enteros
        if self.x.is_integer() and self.y.is_integer() and self.z.is_integer():
            return f"({int(self.x)}, {int(self.y)}, {int(self.z)})"
        return f"({self.x}, {self.y}, {self.z})"

def ingresar_vector(numero):
    while True:
        try:
            entrada = input(f"\nIngrese el vector {numero} (x, y, z): ")
            valores = [float(v.strip()) for v in entrada.split(',')]
            if len(valores) != 3:
                print("Debe ingresar exactamente 3 valores")
                continue
            return VectorTridimensional(*valores)
        except ValueError:
            print("Debe ingrese valores numéricos válidos separados por comas")

def main():
    vector1 = ingresar_vector("A")
    vector2 = ingresar_vector("B")

    while True:
        try:
            escalar = float(input("\nIngrese un valor escalar: "))
            break
        except ValueError:
            print("Ingrese un valor numérico válido")

    print(f"Suma: {vector1 + vector2}")
    print(f"Multiplicación por escalar: {escalar * vector1}")
    print(f"Producto escalar: {vector1 @ vector2:.4f}")
    print(f"Producto vectorial: {vector1 ^ vector2}")
    print(f"Longitud de A: {vector1.longitud():.4f}")
    print(f"Vector normalizado de A: {vector1.normalizar()}")
    print(f"Longitud de B: {vector2.longitud():.4f}")
    print(f"Vector normalizado de B: {vector2.normalizar()}")
    print(f"Proyección ortogonal: {vector1.proyeccion_ortogonal(vector2)}")

if __name__ == "__main__":
    main()