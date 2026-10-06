# Ejercicio 11. Estudiante y sus materias
# Una institución quiere llevar el registro académico de un estudiante.
# Modelá una clase Estudiante que guarde su nombre y las notas de las materias que cursa, y que pueda informar su promedio y si está aprobado o no.

class Estudiante:
    def __init__(self, nombre, nota_minima=60):
        self.nombre = nombre
        self.notas = {}
        self.nota_minima = nota_minima

    def registrar_nota(self, materia, nota):
        self.notas[materia] = nota

    def calcular_promedio(self):
        if not self.notas:
            return 0
        return sum(self.notas.values()) / len(self.notas)

    def esta_aprobado(self):
        return self.calcular_promedio() >= self.nota_minima

    def mostrar_boletin(self):
        print(f"Boletín Académico de {self.nombre}")
        for materia, nota in self.notas.items():
            print(f" - {materia}: {nota}")
        promedio = self.calcular_promedio()
        if self.esta_aprobado():
            condicion = "Aprobado"
        else:
            condicion = "Reprobado"
        print(f"Promedio: {promedio:.2f}")
        print(f"Condición final: {condicion}")

    def __str__(self):
        return f"Estudiante: {self.nombre} | Promedio: {self.calcular_promedio():.2f}"

if __name__ == "__main__":
    estudiante = Estudiante("Tobias Solange")
    
    estudiante.registrar_nota("Programación Avanzada", 85)
    estudiante.registrar_nota("Matemática II", 70)
    estudiante.registrar_nota("Base de Datos", 90)

    estudiante.mostrar_boletin()