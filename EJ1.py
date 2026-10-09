# Ejercicio 1. Ficha de cliente
# Un comercio necesita registrar a sus clientes.
# Modelá una clase que represente a un Cliente con sus datos personales básicos (por ejemplo nombre, cédula y teléfono)
# Y que pueda mostrar su ficha completa en pantalla.

class Cliente:
    def __init__(self, nombre, cedula, telefono):
        self.nombre = nombre
        self.cedula = cedula
        self.telefono = telefono

    def __str__(self):
        return f"Cliente: {self.nombre} | Cédula: {self.cedula} | Teléfono: {self.telefono}"

if __name__ == "__main__":
    cliente_1 = Cliente("Elias", "1728394051", "0981234567")
    cliente_2 = Cliente("Lucas", "1738495062", "0987654321")
    
    print("Fichas de los Clientes:")
    print(cliente_1)
    print(cliente_2)