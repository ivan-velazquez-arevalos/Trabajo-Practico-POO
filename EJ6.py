# Ejercicio 6. Caja registradora de una cuenta corriente
# Un cliente tiene una cuenta en un comercio donde puede cargar saldo y hacer compras.
# Modelá una clase que permita acreditar dinero y registrar consumos, cuidando que el cliente nunca pueda gastar más de lo que tiene.

class CuentaCorriente:
    def __init__(self, cliente, saldo_inicial=0):
        self.cliente = cliente
        self.saldo = saldo_inicial

    def acreditar(self, monto):
        if monto > 0:
            self.saldo += monto
            print(f"Se acreditaron {monto:,.0f} Gs. a la cuenta de {self.cliente}.")
        else:
            print("El monto a acreditar debe ser mayor a cero.")

    def registrar_consumo(self, monto):
        if monto <= 0:
            print("El monto del consumo debe ser mayor a cero.")
        elif monto > self.saldo:
            print(f"Fondos insuficientes para realizar el cosnsumo de {monto:,.0f} Gs.")
        else:
            self.saldo -= monto
            print(f"Se registró el consumo de {monto:,.0f} Gs.")

    def __str__(self):
        return f"Cliente: {self.cliente} | Saldo actual: {self.saldo:,.0f} Gs."

if __name__ == "__main__":
    cuenta = CuentaCorriente("Ivan Emanuel", 100000)
    print(cuenta)

    cuenta.acreditar(50000)
    print(cuenta)

    cuenta.registrar_consumo(80000)
    print(cuenta)

    cuenta.registrar_consumo(100000)
    print(cuenta)