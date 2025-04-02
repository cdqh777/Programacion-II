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

    def validaNumero(self, numero):
        return 0 <= numero <= 10

    def juega(self):
        self.reiniciaPartida()
        self.numeroAAdivinar = random.randint(0, 10)

        print("\nAdivina un número entre 0 y 10")

        while True:
            try:
                numero = int(input("Introduce tu número: "))
            except ValueError:
                print("Por favor, introduce un número válido.")
                continue

            if not self.validaNumero(numero):
                print("Número no válido. Debe estar entre 0 y 10.")
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


class JuegoAdivinaPar(JuegoAdivinaNumero):
    def validaNumero(self, numero):
        if not super().validaNumero(numero):
            print("Número no válido. Debe estar entre 0 y 10.")
            return False
        if numero % 2 != 0:
            print("Error: El número debe ser par.")
            return False
        return True

    def juega(self):
        self.reiniciaPartida()
        self.numeroAAdivinar = random.randint(0, 5) * 2

        print("\nAdivina un número PAR entre 0 y 10")

        while True:
            try:
                numero = int(input("Introduce tu número: "))
            except ValueError:
                print("Por favor, introduce un número válido.")
                continue

            if not self.validaNumero(numero):
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


class JuegoAdivinaImpar(JuegoAdivinaNumero):
    def validaNumero(self, numero):
        if not super().validaNumero(numero):
            print("Número no válido. Debe estar entre 0 y 10.")
            return False
        if numero % 2 == 0:
            print("Error: El número debe ser impar.")
            return False
        return True

    def juega(self):
        self.reiniciaPartida()
        self.numeroAAdivinar = random.randint(0, 4) * 2 + 1

        print("\nAdivina un número IMPAR entre 0 y 10")

        while True:
            try:
                numero = int(input("Introduce tu número: "))
            except ValueError:
                print("Por favor, introduce un número válido.")
                continue

            if not self.validaNumero(numero):
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
        juegos = [
            JuegoAdivinaNumero(3),
            JuegoAdivinaPar(3),
            JuegoAdivinaImpar(3)
        ]

        for juego in juegos:
            juego.juega()


if __name__ == "__main__":
    Aplicacion.main()