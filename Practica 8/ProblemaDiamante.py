class A:
    def metodo(self):
        print("Método de A")

class B(A):
    def metodo(self):
        print("Método de B")
        super().metodo()

class C(A):
    def metodo(self):
        print("Método de C")
        super().metodo()

class D(B, C):
    def metodo(self):
        print("Método de D")
        super().metodo()


print(D.mro())
D().metodo()