# Clase Padre
class Empleado:
    def __init__(self, nombre, legajo):
        self.nombre = nombre
        self.legajo = legajo

    def getDetails(self):
        print("Nombre empleado: " + self.nombre)
        legajoAux = str(self.legajo)
        print('Legajo empleado: ' + legajoAux)

    def getNombre(self):
        return self.nombre

    def getLegajo(self):
        return self.legajo


# herencia
class QAautomation(Empleado):
    # constructor clase hija, utiliza el constructor del padre para los atributos que recibe por
    # herencia
    def __init__(self, tareas, antiguedad, nombre, legajo):
        self.tareas = tareas
        self.antiguedad = antiguedad
        Empleado.__init__(self, nombre, legajo)

    # metodo nuevo de la clase hija
    def getMostrarTareas(self):
        print("Las tareas del QA automation son: " + self.tareas)


# herencia otra clase que hereda de Empleado
class Desarrollador(Empleado):
    # constructor clase hija, utiliza el constructor del padre para los atributos que recibe por
    # herencia
    def __init__(self, proyecto, antiguedad, nombre, legajo):
        self.proyecto = proyecto
        self.antiguedad = antiguedad
        Empleado.__init__(self, nombre, legajo)

    # metodo nuevo de la clase hija
    def getMostrarProyectos(self):
        print("El proyecto del desarrollador es: " + self.proyecto)


desarrolador_1 = Desarrollador("IBM", 3, "Marcos", 1234)
automationQA = QAautomation("Cargar bugs", 5, "Pablo", 2345)


print("*************************************************")
print("Mostramos datos del desarrollador de la empresa: ")
desarrolador_1.getDetails()
desarrolador_1.getMostrarProyectos()
print("Nombre Empleado utilizando un get de la propiedad: " + desarrolador_1.getNombre())
print("*************************************************")
print("Mostramos datos del QA automation de la empresa: ")
automationQA.getDetails()
automationQA.getMostrarTareas()
print("Nombre Empleado utilizando un get de la propiedad: " + automationQA.getNombre())
print("*************************************************")


