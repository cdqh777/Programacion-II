import math

def promedio(datos):
    return sum(datos) / len(datos)

def desviacion(datos, promedio):
    varianza = sum((x - promedio) ** 2 for x in datos) / (len(datos) - 1)
    return math.sqrt(varianza)

datos = list(map(float, input().split()))
prom = promedio(datos)
desv = desviacion(datos, prom)

print(f"El promedio es {prom:.2f}")
print(f"La desviación estándar es {desv:.5f}")
