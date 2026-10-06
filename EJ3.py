# Ejercicio 3. Empleado y su sueldo
# Una empresa necesita representar a sus empleados.
# Modelá una clase Empleado con su nombre, cargo y salario mensual.
# La clase debe poder informar cuánto cobra ese empleado en un año

class Empleado:
    def __init__(self, nombre, cargo, salario_mensual):
        self.nombre = nombre
        self.cargo = cargo
        self.salario_mensual = salario_mensual

    def calcular_salario_anual(self, aguinaldo = True):
        if aguinaldo:
            meses = 13
        else:
            meses = 12
        return self.salario_mensual * meses

    def __str__(self):
        anual = self.calcular_salario_anual()
        return f"Empleado: {self.nombre} | Cargo: {self.cargo} | Salario Mensual: ₲{self.salario_mensual:,.0f} | Salario Anual (+Aguinaldo): ₲{anual:,.0f}"

if __name__ == "__main__":
    emp = Empleado("Jose Roberto", "Desarrollador en Python", 6000000)

    print("Datos de Empleado")
    print(emp)

    print("\nSalario Anual del Empleado:")
    print(f"{emp.nombre} (Sin aguinaldo): ₲{emp.calcular_salario_anual(aguinaldo=False):,.0f}")
    print(f"{emp.nombre} (Con aguinaldo): ₲{emp.calcular_salario_anual(aguinaldo=True):,.0f}")