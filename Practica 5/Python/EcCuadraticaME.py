import math

def resolverEcuacionCuadratica(a, b, c):
    discriminante = b ** 2 - 4 * a * c

    if discriminante > 0:
        r1 = (-b + math.sqrt(discriminante)) / (2 * a)
        r2 = (-b - math.sqrt(discriminante)) / (2 * a)
        return f"La ecuación tiene dos raíces {formatear(r1, 6)} y {formatear(r2, 5)}"

    elif discriminante == 0:
        r1 = -b / (2 * a)
        return f"La ecuación tiene una raíz {formatear(r1, 0)}"

    else:
        return "La ecuación no tiene raíces reales"


def formatear(valor, decimales):
    return f"{valor:.{decimales}f}"

a, b, c = map(float, input("Ingrese a, b, c: ").split())
print(resolverEcuacionCuadratica(a, b, c))
