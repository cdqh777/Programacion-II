import math
import random
from abc import ABC, abstractmethod


class Coloreado(ABC):
    @abstractmethod
    def comoColorear(self) -> str:
        pass


class Figura(ABC):
    def __init__(self, color: str):
        self.color = color

    def setColor(self, color: str):
        self.color = color

    def getColor(self) -> str:
        return self.color

    def __str__(self) -> str:
        return f"Figura de color {self.color}"

    @abstractmethod
    def area(self) -> float:
        pass

    @abstractmethod
    def perimetro(self) -> float:
        pass


class Cuadrado(Figura, Coloreado):
    def __init__(self, color: str, lado: float):
        super().__init__(color)
        self.lado = round(lado, 2)

    def area(self) -> float:
        return round(self.lado ** 2, 2)

    def perimetro(self) -> float:
        return round(4 * self.lado, 2)

    def comoColorear(self) -> str:
        return "Colorear los cuatro lados"

    def __str__(self) -> str:
        return f"Cuadrado de lado {self.lado:.2f} y color {self.getColor()}"


class Circulo(Figura):
    def __init__(self, color: str, radio: float):
        super().__init__(color)
        self.radio = round(radio, 2)

    def area(self) -> float:
        return round(math.pi * (self.radio ** 2), 2)

    def perimetro(self) -> float:
        return round(2 * math.pi * self.radio, 2)

    def __str__(self) -> str:
        return f"Círculo de radio {self.radio:.2f} y color {self.getColor()}"


def main():
    figuras = []
    colores = ["rojo", "verde", "azul", "amarillo", "negro", "blanco"]

    for _ in range(5):
        tipo_figura = random.randint(1, 2)
        color = random.choice(colores)

        if tipo_figura == 1:  # Cuadrado
            lado = random.uniform(1.0, 10.0)
            figuras.append(Cuadrado(color, lado))
        else:
            radio = random.uniform(1.0, 10.0)
            figuras.append(Circulo(color, radio))

    for figura in figuras:
        print("\n" + "-" * 50)
        print(f"Figura: {figura}")
        print(f"Área: {figura.area():.2f}")
        print(f"Perímetro: {figura.perimetro():.2f}")

        if isinstance(figura, Coloreado):
            print(f"Método colorear: {figura.comoColorear()}")


if __name__ == "__main__":
    main()