import random


class Juego:
    def __init__(self, numeroDeVidas):
        self.numeroDeVidas = numeroDeVidas
        self.record = 0

    def reiniciaPartida(self):
        self.numeroDeVidas = self.record if self.record > 0 else self.numeroDeVidas

    def actualizaRecord(self):
        if self.numeroDeVidas > self.record:
            self.record = self.numeroDeVidas

    def quitaVida(self):
        self.numeroDeVidas -= 1
        return self.numeroDeVidas > 0


class JuegoAdivinaNumero(Juego):
    def __init__(self, numeroDeVidas):
        super().__init__(numeroDeVidas)
        self.numeroAAdivinar = 0

    def juega(self):
        self.reiniciaPartida()
        self.numeroAAdivinar = random.randint(0, 10)

        print("Adivina un número entre 0 y 10")

        while True:
            try:
                numero = int(input("Introduce tu número: "))
            except ValueError:
                print("Por favor, introduce un número válido.")
                continue

            if numero == self.numeroAAdivinar:
                print("Acertaste!!")
                self.actualizaRecord()
                break
            else:
                if not self.quitaVida():
                    print(f"¡Game over! El número era {self.numeroAAdivinar}")
                    break
                else:
                    if numero < self.numeroAAdivinar:
                        print("El número a adivinar es mayor. Inténtalo de nuevo.")
                    else:
                        print("El número a adivinar es menor. Inténtalo de nuevo.")
                    print(f"Te quedan {self.numeroDeVidas} vidas.")


class Aplicacion:
    def main():
        juego = JuegoAdivinaNumero(3)
        juego.juega()


if __name__ == "__main__":
    Aplicacion.main()