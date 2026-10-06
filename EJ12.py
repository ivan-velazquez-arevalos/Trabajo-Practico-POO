# Ejercicio 12. Cuenta de servicio con planes
# Una empresa de telefonía ofrece a sus clientes un plan con una cantidad de gigabytes incluidos.
# Modelá una clase que represente la línea de un cliente, controle el consumo de datos y avise cuando se agota el paquete contratado.

class LineaTelefonica:
    def __init__(self, titular, giga_plan):
        self.titular = titular
        self.giga_plan = giga_plan
        self.giga_consumidos = 0

    def obtener_disponibles(self):
        disponible = self.giga_plan - self.giga_consumidos
        return max(0, disponible)

    def registrar_consumo(self, gigas):
        if self.obtener_disponibles() == 0:
            print(f"No se puede consumir {gigas} GB. El paquete de datos se agotó.")
        elif self.giga_consumidos + gigas > self.giga_plan:
            print(f"El consumo de {gigas} GB supera el saldo disponible. Paquete agotado.")
            self.giga_consumidos = self.giga_plan
        else:
            self.giga_consumidos += gigas
            print(f"Se consumieron {gigas} GB. GB Disponibles: {self.obtener_disponibles()}.")

    def __str__(self):
        return f"Titular: {self.titular} | Plan: {self.giga_plan} GB | GB Consumidos: {self.giga_consumidos} | GB Disponibles: {self.obtener_disponibles()}"

if __name__ == "__main__":
    linea = LineaTelefonica("Hugo Gomez", 10)
    print(linea)

    linea.registrar_consumo(4)
    linea.registrar_consumo(5)
    linea.registrar_consumo(3)
    linea.registrar_consumo(1)

    print(linea)