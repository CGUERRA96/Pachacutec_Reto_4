class Persona():
    def __init__(self, dni, nombre, edad):
        self.dni = dni
        self.nombre = nombre
        self.edad = edad

class Docente(Persona):
    def __init__(self, dni, nombre, edad):
        self.dni = dni
        self.nombre = nombre
        self.edad = edad

class Alumno(Persona):
    def __init__ (self, dni, nombre, edad, nota, notami, notamax, notaprom):
        self.dni = dni
        self.nombre = nombre
        self.edad = edad
        self.nota = nota
        self.notami = notami
        self.notamax = notamax
        self.notaprom = notaprom