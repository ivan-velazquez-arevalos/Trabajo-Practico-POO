# Ejercicio 9. Turnos de un consultorio
# Un consultorio necesita gestionar los turnos del día.
# Una clase representa un Turno (paciente, hora y estado) y otra clase, la Agenda, administra todos los turnos de la jornada:
# Permite agendar nuevos turnos y listar los pendientes.

class Turno:
    def __init__(self, paciente, hora, estado="pendiente"):
        self.paciente = paciente
        self.hora = hora
        self.estado = estado

    def marcar_atendido(self):
        self.estado = "atendido"

    def __str__(self):
        return f"Paciente: {self.paciente} | Hora: {self.hora} | Estado: {self.estado}"

class Agenda:
    def __init__(self, fecha):
        self.fecha = fecha
        self.turnos = []

    def agendar_turno(self, turno):
        self.turnos.append(turno)

    def listar_pendientes(self):
        print(f"Turnos pendientes para el {self.fecha}:")
        for turno in self.turnos:
            if turno.estado == "pendiente":
                print(f" - {turno}")

if __name__ == "__main__":
    t1 = Turno("Maria Celeste", "08:00")
    t2 = Turno("Fernando Daniel", "09:00")
    t3 = Turno("Valerie Nicole", "10:00")

    agenda = Agenda("10/10/2026")
    agenda.agendar_turno(t1)
    agenda.agendar_turno(t2)
    agenda.agendar_turno(t3)

    t1.marcar_atendido()

    agenda.listar_pendientes()