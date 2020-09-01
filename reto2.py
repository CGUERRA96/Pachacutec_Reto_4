from time import sleep
#from pj import persona
import json

data_docente = {}
data_alumno = {}

data_docente['docentes_creados'] = []
data_alumno['alumnos_creados'] = []

class Docente():
    def __init__(self, dni, nombre, edad):
        self.dni = dni
        self.nombre = nombre
        self.edad = edad

    def obtener_docente(self):
        
        self.dni = input("Ingrese el DNI: "),
        self.nombre = input('Ingrese nombre del docente: '),
        self.edad = int(input("Ingrese su edad: "))
        docente = Docente( self.dni, self.nombre, self.edad)
        datos = {
            "Nombre": docente.nombre,
            "DNI": docente.dni,
            "Edad": docente.edad
        }
        self.guardar_docente(datos)
        print(f"\nEl docente {self.nombre} ha sido creado")

    def guardar_docente(self, datos):
        data_docente['docentes_creados'].append(datos)
        pjs_docente = data_docente['docentes_creados']
        archivo_docente = open('docente.json', "w")
        json.dump(pjs_docente, archivo_docente, indent= 4)
    
    def cargar_docente(self):
        try:
            archivo_docente = open('docente.json')
            data_docente['docentes_creados'] = json.load(archivo_docente)
        except FileNotFoundError:
            print("\nCreado registro de docentes!! ....")
            archivo_docente = open("docente.json", "a+")
        except json.decoder.JSONDecodeError:
            print("\nNo hay docentes creados, se puede empezar desde ahora.")
    
    def mostrar_docentes(self):
        if data_docente['docentes_creados'] == []:
            print("\nNo se encuentran personajes creados")

        for docente in data_docente['docentes_creados']:
            print(f'''
                DNI: {docente['DNI']},
                Nombre: {docente['Nombre']},
                Edad: {docente['Edad']}
            ''')
class Alumno(Docente):
    def __init__ (self, dni, nombre, edad, nota):
        self.dni = dni
        self.nombre = nombre
        self.edad = edad
        self.nota = nota

    def obtener_alumno(self):

        cant_alumnos = int(input('Cuantos alumnos se agregara?: '))
        for a in range(cant_alumnos):
            self.dni = input('Ingrese el DNI: ')
            self.nombre = input('Ingrese nombre del alumno: ')
            self.edad = int(input('Ingrese su edad: '))
            while True:

                cant_notas = int(input('Ingrese cantidad de notas: '))
                if cant_notas >= 0 and cant_notas<=4:
                    lista_nota = []
                    for n in range(cant_notas):
                            while True:
                                self.nota = int(input(f"Ingrese la nota {n + 1}:"))
                                if  self.nota >= 0 and self.nota <= 20:
                                    lista_nota.append(self.nota)
                                    break
                                else:
                                    print('Ingresar una nota entre 00 al 20')
                    break
                    datos_alumo = {
                        'DNI': self.dni,
                        'Nombre': self.nombre,
                        'Edad': self.edad,
                        'Notas': self.nota,
                        'Notasmin': min(self.nota),
                        'Notamax': max(self.nota),
                        'Notaprom': sum(self.nota)/len(self.nota)
                    }
                    self.guardar_alumno(datos_alumo)
                else:
                    print("Ingresar un numero del 1 al 4")

    def guardar_alumno(self, datos_alumo):
        data_alumno['alumnos_creados'].append(datos_alumo)
        pjs_alumno = data_alumno['alumnos_creados']
        archivo_alumno = open('alumno.json', "w")
        json.dump(pjs_alumno, archivo_alumno, indent= 4)

    def cargar_alumno(self):
        try:
            archivo_alumno = open('alumno.json')
            data_alumno['alumnos_creados'] = json.load(archivo_alumno)
        except FileNotFoundError:
            print("\nCreado registro de alumno!! ....")
            archivo_alumno = open("alumno.json", "a+")
        except json.decoder.JSONDecodeError:
            print("\nNo hay alumnos creados, se puede empezar desde ahora.")

    def mostrar_alumno(self):

        if data_alumno['alumnos_creados'] == []:
            print("\nNo se encuentran personajes creados")

        for alumno in data_alumno['alumnos_creados']:
            print(f'''
                DNI: {alumno['DNI']},
                Nombre: {alumno['Nombre']},
                Edad: {alumno['Edad']},
                Nota: {alumno['Nota']},
                Notasmin: {alumno['Notasmin']},
                Notamax: {alumno['Notamax']},
                Notaprom: {alumno['Notaprom']}
            ''')

    def interfaz(self,):
        while True:
            print('''\nBienvenido al Menú
             ¿Que deseas hacer?
             1) Crear un docente
             2) Mostrar docentes
             3) Crear un alumno
             4) Mostrar alumnos
             5) Crear un curso
             6) Salir del programa''')
            opcion = input("> ")
            if opcion == "1":
                self.obtener_docente()
            elif opcion == "2":
                self.mostrar_docentes()
            elif opcion == "3":
                self.obtener_alumno()
            elif opcion == "4":
                self.mostrar_alumno()
            elif opcion == "6":
                print('\nGracias por usar esta aplicación\n')
                sleep(2)
                quit()
            else:
                print('\nHas introducido una opción erronea')

class Inicio(Alumno):
    def __init__(self):
        self.cargar_docente()
        self.cargar_alumno()
        self.interfaz()

Inicio()
