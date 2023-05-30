
class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def imprimir_informacion(self):
        print("Nombre:", self.nombre)
        print("Nota:", self.nota)

    def resultado_aprobacion(self):
        if self.nota >= 6:
            print("¡El alumno aprobó!")
        else:
            print("El alumno reprobó.")


alumno1 = Alumno("Juan", 7.5)
alumno1.imprimir_informacion()
alumno1.resultado_aprobacion()
