# Ejercicio 2. Producto de almacén
# Un almacén quiere representar los productos que vende.
# Modelá una clase Producto con su nombre, precio unitario y cantidad en stock.
# La clase debe poder informar el valor total de las unidades en stock (precio por cantidad).

class Producto:
    def __init__(self, nombre, precio_unitario, stock):
        self.nombre = nombre
        self.precio_unitario = precio_unitario
        self.stock = stock

    def calcular_valor_total(self):
        return self.precio_unitario * self.stock

    def __str__(self):
        valor_total = self.calcular_valor_total()
        return f"Producto: {self.nombre} | Precio: {self.precio_unitario:.2f} | Stock: {self.stock} | Valor Total: {valor_total:.2f}"

if __name__ == "__main__":
    prod1 = Producto("Arroz 1kg", 8000.0, 20)
    prod2 = Producto("Aceite de Girasol 1L", 10000.0, 15)
    prod3 = Producto("Leche Entera 1L", 8000.0, 30)

    print("Productos del Almacén")
    print(prod1)
    print(prod2)
    print(prod3)

    print("\nValor Total de los Productos en Stock:")
    print(f"Total acumulado de {prod1.nombre}: ${prod1.calcular_valor_total():.2f}")
    print(f"Total acumulado de {prod2.nombre}: ${prod2.calcular_valor_total():.2f}")
    print(f"Total acumulado de {prod3.nombre}: ${prod3.calcular_valor_total():.2f}")