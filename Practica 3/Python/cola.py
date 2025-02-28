class Cola:
    def __init__(self):
        self.__elementos = []

    def encolar(self, elemento):
        self.__elementos.append(elemento)

    def desencolar(self):
        if self.esta_vacia():
            raise IndexError("La cola está vacía")
        return self.__elementos.pop(0)

    def esta_vacia(self):
        return len(self.__elementos) == 0

    def ver_frente(self):
        if self.esta_vacia():
            raise IndexError("La cola está vacía")
        return self.__elementos[0]

    def __str__(self):
        return str(self.__elementos)


cola = Cola()
cola.encolar(10)
cola.encolar(20)
cola.encolar(30)
print("Cola:", cola)
print("Frente:", cola.ver_frente())
print("Desencoladas:", cola.desencolar())
print("Cola sin desencolar:", cola)