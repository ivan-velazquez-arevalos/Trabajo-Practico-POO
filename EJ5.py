# Ejercicio 5. Vehículo de una agencia
# Una agencia automotriz registra los vehículos que tiene a la venta.
# Modelá una clase Vehiculo con su marca, modelo, año y precio.
# La clase debe poder informar una descripción comercial del vehículo lista para publicar.

class Vehiculo:
    def __init__(self, marca, modelo, anio, precio):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.precio = precio

    def obtener_descripcion_comercial(self):
        return f"{self.marca} {self.modelo} {self.anio} — {self.precio:,.0f} Gs.".replace(",", ".")

    def __str__(self):
        return self.obtener_descripcion_comercial()

if __name__ == "__main__":
    vehiculo1 = Vehiculo("Toyota", "Corolla", 2020, 95000000)
    vehiculo2 = Vehiculo("Hyundai", "HB20", 2022, 75000000)

    print(vehiculo1)
    print(vehiculo2)