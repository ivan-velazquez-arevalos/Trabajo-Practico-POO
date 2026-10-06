# Ejercicio 13. Habitación de un hotel
# Un hotel necesita gestionar la ocupación de sus habitaciones.
# Modelá una clase Habitacion con su número, tipo y tarifa por noche, que pueda ocuparse y liberarse, y calcular el costo de una estadía según la cantidad de noches.

class Habitacion:
    def __init__(self, numero, tipo, tarifa_por_noche):
        self.numero = numero
        self.tipo = tipo
        self.tarifa_por_noche = tarifa_por_noche
        self.ocupada = False

    def ocupar(self):
        if self.ocupada:
            print(f"La habitación {self.numero} ya esta ocupada.")
        else:
            self.ocupada = True
            print(f"La habitación {self.numero} ha sido ocupada.")

    def liberar(self):
        if not self.ocupada:
            print(f"La habitación {self.numero} ya está libre.")
        else:
            self.ocupada = False
            print(f"La habitación {self.numero} ha sido liberada.")

    def calcular_costo_estadia(self, noches):
        return self.tarifa_por_noche * noches

    def __str__(self):
        if self.ocupada:
            estado = "Ocupada"
        else:
            estado = "Libre"
        return f"Habitación {self.numero} ({self.tipo}) | Tarifa: {self.tarifa_por_noche:,.0f} Gs. | Estado: {estado}"

if __name__ == "__main__":
    h = Habitacion(69, "Matrimonial", 250000)
    print(h)

    h.ocupar()
    h.ocupar()

    noches = 3
    costo = h.calcular_costo_estadia(noches)
    print(f"Costo por {noches} noches: {costo:,.0f} Gs.")

    h.liberar()
    print(h)