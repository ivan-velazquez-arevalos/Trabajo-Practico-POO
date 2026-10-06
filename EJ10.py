# Ejercicio 10. Carrito de compras de un e-commerce
# Modelá el carrito de compras de una tienda en línea.
# Una clase representa un Item (producto y cantidad) y otra, el Carrito, reúne los ítems que el cliente va agregando.
# El carrito debe calcular el total a pagar.

class Producto:
    def __init__(self, nombre, precio_unitario):
        self.nombre = nombre
        self.precio_unitario = precio_unitario

    def __str__(self):
        return f"{self.nombre} - {self.precio_unitario:,.0f} Gs."

class Item:
    def __init__(self, producto, cantidad):
        self.producto = producto
        self.cantidad = cantidad

    def calcular_subtotal(self):
        return self.producto.precio_unitario * self.cantidad

    def __str__(self):
        return f"{self.producto.nombre} x {self.cantidad} = {self.calcular_subtotal():,.0f} Gs."

class Carrito:
    def __init__(self):
        self.items = []

    def agregar_item(self, item):
        self.items.append(item)

    def calcular_total(self):
        total = 0
        for item in self.items:
            total += item.calcular_subtotal()
        return total

    def mostrar_detalle(self):
        print("Detalle de la compra:")
        for item in self.items:
            print(f" - {item}")
        print(f"Total general: {self.calcular_total():,.0f} Gs.")

    def __str__(self):
        return f"Carrito con {len(self.items)} ítems | Total: {self.calcular_total():,.0f} Gs."

if __name__ == "__main__":
    p1 = Producto("Auriculares Bluetooth", 150000)
    p2 = Producto("Cargador Portatil", 80000)

    i1 = Item(p1, 2)
    i2 = Item(p2, 1)

    carrito = Carrito()
    carrito.agregar_item(i1)
    carrito.agregar_item(i2)

    carrito.mostrar_detalle()