class Artista:
    def __init__(self, nombre, anosExperiencia):
        self.nombre = nombre
        self.anosExperiencia = anosExperiencia


class Anuncio:
    def __init__(self, numero, precio):
        self.numero = numero
        self.precio = precio
        self.precioOriginal = precio

    def incrementarPrecio(self, incremento):
        self.precio += incremento


class Obra:
    def __init__(self, titulo, material, artista1, artista2=None, anuncio=None):
        self.titulo = titulo
        self.material = material
        self.artista1 = artista1
        self.artista2 = artista2
        self.anuncio = anuncio

    def agregarAnuncio(self, numero, precio):
        self.anuncio = Anuncio(numero, precio)

    def artistaConMasExperiencia(self):
        artistas = [self.artista1]
        if self.artista2:
            artistas.append(self.artista2)
        return max(artistas, key=lambda x: x.anosExperiencia).nombre

    def montoVenta(self):
        return self.anuncio.precio if self.anuncio else 0

    def promedioExperienciaArtistas(self):
        total = self.artista1.anosExperiencia
        count = 1
        if self.artista2:
            total += self.artista2.anosExperiencia
            count += 1
        return total / count

    def incrementarPrecioArtista(self, nombreArtista, incremento):
        if self.artista1.nombre == nombreArtista or (self.artista2 and self.artista2.nombre == nombreArtista):
            if self.anuncio:
                self.anuncio.incrementarPrecio(incremento)
                return True
        return False

    def obtenerPrecio(self):
        return self.anuncio.precio if self.anuncio else 0


def resolverParcialA():
    print("\n PARCIAL A")

    artistaA1 = Artista("Pablo Picasso", 50)
    artistaA2 = Artista("Vincent van Gogh", 30)

    pinturaConAnuncio = Obra(
        titulo="Guernica",
        material="Óleo sobre lienzo",
        artista1=artistaA1,
        artista2=artistaA2,
        anuncio=Anuncio(1, 1000000)
    )

    pinturaSinAnuncio = Obra(
        titulo="La noche estrellada",
        material="Óleo sobre lienzo",
        artista1=artistaA2
    )

    print("\n1a. Pinturas creadas:")
    print(f"- {pinturaConAnuncio.titulo} (con anuncio)")
    print(f"- {pinturaSinAnuncio.titulo} (sin anuncio)")

    def artistaMasExperiencia(p1, p2):
        artistas = [p1.artista1]
        if p1.artista2: artistas.append(p1.artista2)
        artistas += [p2.artista1]
        if p2.artista2: artistas.append(p2.artista2)
        return max(artistas, key=lambda x: x.anosExperiencia).nombre

    print("\n1b. Artista con más experiencia:", artistaMasExperiencia(pinturaConAnuncio, pinturaSinAnuncio))

    pinturaSinAnuncio.agregarAnuncio(2, 500000)
    total = pinturaConAnuncio.montoVenta() + pinturaSinAnuncio.montoVenta()
    print("\n1c. Monto total de venta:", f"${total:,}")


def resolverParcialB():
    print("\n PARCIAL B")

    artistaB1 = Artista("Claude Monet", 40)
    artistaB2 = Artista("Salvador Dalí", 35)
    artistaB3 = Artista("Frida Kahlo", 30)
    artistaB4 = Artista("Diego Rivera", 45)

    pinturaB1 = Obra(
        titulo="Impresión, sol naciente",
        material="Óleo sobre lienzo",
        artista1=artistaB1,
        artista2=artistaB2,
        anuncio=Anuncio(1, 2000000)
    )

    pinturaB2 = Obra(
        titulo="La persistencia de la memoria",
        material="Óleo sobre lienzo",
        artista1=artistaB3,
        artista2=artistaB4,
        anuncio=Anuncio(2, 1500000)
    )

    print("\n1a. Pinturas con anuncios:")
    print(f"- {pinturaB1.titulo} (${pinturaB1.obtenerPrecio():,})")
    print(f"- {pinturaB2.titulo} (${pinturaB2.obtenerPrecio():,})")

    promedio = (pinturaB1.promedioExperienciaArtistas() + pinturaB2.promedioExperienciaArtistas()) / 2
    print("\n1b. Promedio de experiencia:", f"{promedio:.1f} años")

    artista = "Frida Kahlo"
    incremento = 500000
    for p in [pinturaB1, pinturaB2]:
        if p.incrementarPrecioArtista(artista, incremento):
            print(f"\n1c. Precio de '{p.titulo}' incrementado en ${incremento:,}")
            print("Nuevo precio:", f"${p.obtenerPrecio():,}")


if __name__ == "__main__":
    resolverParcialA()
    resolverParcialB()