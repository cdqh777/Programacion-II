class Pila:
    def __init__(self):
        self.__elementos = []

    def apilar(self, elemento):
        self.__elementos.append(elemento)

    def desapilar(self):
        if self.esta_vacia():
            raise IndexError("La pila está vacía")
        return self.__elementos.pop()

    def esta_vacia(self):
        return len(self.__elementos) == 0

    def ver_tope(self):
        if self.esta_vacia():
            raise IndexError("La pila está vacía")
        return self.__elementos[-1]

    def __str__(self):
        return str(self.__elementos)


pila = Pila()
pila.apilar(10)
pila.apilar(20)
pila.apilar(30)
print("Pila:", pila)
print("Tope:", pila.ver_tope())
print("Desapiladas:", pila.desapilar())
print("Pilas restantes:", pila)