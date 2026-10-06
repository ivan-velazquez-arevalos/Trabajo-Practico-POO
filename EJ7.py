# Ejercicio 7. Control de stock con alertas
# Retomá la idea del producto de almacén, pero ahora el producto debe manejar su propio stock a lo largo del tiempo:
# Se reponen unidades cuando llega mercadería y se descuentan cuando se vende.
# Además, debe avisar cuando el stock queda por debajo de un mínimo.

class Producto:
    def __init__(self, nombre, precio, stock, stock_minimo):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        self.stock_minimo = stock_minimo

    def ingresar_mercaderia(self, cantidad):
        if cantidad > 0:
            self.stock += cantidad
            print(f"Se ingresaron {cantidad} unidades de {self.nombre}.")
        else:
            print("La cantidad a ingresar debe ser mayor a cero.")

    def registrar_venta(self, cantidad):
        if cantidad <= 0:
            print("La cantidad a vender debe ser mayor a cero.")
        elif cantidad > self.stock:
            print(f"No hay suficiente stock de {self.nombre} para vender {cantidad} unidades.")
        else:
            self.stock -= cantidad
            print(f"Se vendieron {cantidad} unidades de {self.nombre}.")
            if self.stock < self.stock_minimo:
                print(f"El Stock de {self.nombre} esta por debajo del Stock mínimo ({self.stock}/{self.stock_minimo}).")

    def __str__(self):
        return f"Producto: {self.nombre} | Precio: {self.precio:,.0f} Gs. | Stock: {self.stock} | Stock Mínimo: {self.stock_minimo}"

if __name__ == "__main__":
    prod = Producto("Yerba Mate 1kg", 18000, 10, 5)
    print(prod)

    prod.registrar_venta(7)
    print(prod)

    prod.ingresar_mercaderia(10)
    print(prod)

    prod.registrar_venta(15)
    print(prod)