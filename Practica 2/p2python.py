import matplotlib.pyplot as plt

class Linea:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __str__(self):
        return f"Linea(p1={self.p1}, p2={self.p2})"

    def dibujalinea(self):
        plt.plot([self.p1[0], self.p2[0]], [self.p1[1], self.p2[1]], marker='o')

class Circulo:
    def __init__(self, centro, radio):
        self.centro = centro
        self.radio = radio

    def __str__(self):
        return f"Circulo(centro={self.centro}, radio={self.radio})"

    def dibujacirculo(self):
        circle = plt.Circle((self.centro[0], self.centro[1]), self.radio, color='blue', fill=False)
        plt.gca().add_patch(circle)

p1 = (1, 2)
p2 = (3, 4)
centro = (0, 0)

linea = Linea(p1, p2)
print(linea)
linea.dibujalinea()

circulo = Circulo(centro, 5)
print(circulo)
circulo.dibujacirculo()

plt.xlim(-10, 10)
plt.ylim(-10, 10)
plt.gca().set_aspect('equal', adjustable='box')
plt.grid(True)
plt.show()
