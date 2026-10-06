# Ejercicio 8. Reproductor de lista de canciones
# Modelá una aplicación sencilla de música.
# Una clase representa una Cancion (título, artista y duración) y otra clase representa una ListaReproduccion que contiene varias canciones.
# La lista debe poder agregar canciones e informar la duración total.

class Cancion:
    def __init__(self, titulo, artista, duracion_segundos):
        self.titulo = titulo
        self.artista = artista
        self.duracion_segundos = duracion_segundos

    def __str__(self):
        minutos = self.duracion_segundos // 60
        segundos = self.duracion_segundos % 60
        return f"'{self.titulo}' - {self.artista} ({minutos}:{segundos:02d})"

class ListaReproduccion:
    def __init__(self, nombre):
        self.nombre = nombre
        self.canciones = []

    def agregar_cancion(self, cancion):
        self.canciones.append(cancion)

    def calcular_duracion_total(self):
        total = 0
        for cancion in self.canciones:
            total += cancion.duracion_segundos
        return total

    def __str__(self):
        salida = f"Lista de Reproducción: {self.nombre}\n"
        for cancion in self.canciones:
            salida += f" - {cancion}\n"
        total_seg = self.calcular_duracion_total()
        minutos = total_seg // 60
        segundos = total_seg % 60
        salida += f"Duración Total: {minutos}:{segundos:02d} mins"
        return salida

if __name__ == "__main__":
    c1 = Cancion("No Pole", "Don Toliver", 188)
    c2 = Cancion("Timeless", "The Weeknd", 256)
    c3 = Cancion("4X4", "Travis Scott", 201)

    mi_lista = ListaReproduccion("Mis Canciones")
    mi_lista.agregar_cancion(c1)
    mi_lista.agregar_cancion(c2)
    mi_lista.agregar_cancion(c3)

    print(mi_lista)