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

class Archivo():
    def __init__(self, nombre_archivo):
        self.nombre_archivo = nombre_archivo

    def mostrar_archivo(self):
        try:
            file = open (self.nombre_archivo, mode='r', encoding='utf-8')
            for linea in file.readlines():
                print(linea)
        except Exception as e:
            print(f'{str(e)}')
        finally:
            if(file):
                file.close()
                print('Se visualiza un archivo')

    def agregar_docente(self, docentes):
        try:
            file = open(self.nombre_archivo, mode='a')
            docentes = f'Docente: {docentes.dni}, {docentes.nombre}, {docentes.edad}\n'
            file.write(docentes)
        except Exception as e:
            print(f'{str(e)}')
        finally:
            if(file):
                file.close()
                print('Se visualiza un docente')

    def agregar_alumno(self, alumno):
        try:
            file = open(self.nombre_archivo, mode='a')
            alumno = f'Alumno: {alumno.dni}, {alumno.nombre}, {alumno.edad}, {alumno.nota}, {alumno.notami}, {alumno.notamax}, {alumno.notaprom}\n'
            file.write(alumno)
        except Exception as e:
            print(f'{str(e)}')
        finally:
            if(file):
                file.close()
                print('Se visualiza un alumno')

print('###########:REGISTRO ACADEMICO:###########')
print('''
    1.- REGISTRAR DOCENTES
    2.- REGISTRAR ALUMNOS
''')

opcion_seleccion = int(input('Seleccione una opción >> ')) 

if opcion_seleccion == 1:    
    cant_docentes = int(input('Cuantos docentes se agregara?: '))
    #persona_nombre = input('Como te llamas?: ')
    #persona_edad = int(input('Cual es su edad: '))
    #persona_sexo = input('Cual es su sexo: ')

    for p in range(cant_docentes):
        docentes_nombre = input('Como te llamas?: ')
        docentes_dni = input('Cual es tu dni?: ')    
        docentes_edad = int(input('Cual es tu edad: '))

        docentes = Docente(docentes_nombre, docentes_dni, docentes_edad)
        archivo = Archivo('docentes.txt')
        archivo.agregar_docente(docentes)
    archivo.mostrar_archivo()

elif opcion_seleccion == 2:
    
    cant_alumnos = int(input('Cuantos alumnos se agregara?: '))
    lista_alumnos = []
    for a in range(cant_alumnos):
        alumno_nombre = []
        alumnos_nombre = input('Como te llamas?: ')
        alumno_dni = []
        alumnos_dni = input('Cual es tu dni?: ')
        alumno_edad = []
        alumnos_edad = int(input('Cual es tu edad: '))
        while True:

            cant_notas = int(input('Ingrese cantidad de notas: '))
            if cant_notas >= 0 and cant_notas<=4:
                lista_nota = []
                for n in range(cant_notas):
                        while True:
                            notas = int(input(f"Ingrese la nota {n + 1}:"))
                            if  notas >= 0 and notas <= 20:
                                lista_nota.append(notas)
                                break
                            else:
                                print('Ingresar una nota entre 00 al 20')

                lista_alumnos.append({
                    'Alumno': {
                        'Nombre': alumnos_nombre,
                        'DNI': alumnos_dni,
                        'Edad': alumnos_edad
                    },
                    'Notas': lista_nota
                })
                break
            else:
                print("Ingresar un numero del 1 al 4")

    for v in lista_alumnos:                    
        alumnos = Alumno(f"{v['Alumno']['DNI']}", f"{v['Alumno']['Nombre']}", f"{v['Alumno']['Edad']}", f"{v['Notas']}", f"{min(v['Notas'])}", f"{max(v['Notas'])}", f"{sum(v['Notas'])/len(v['Notas'])}")
        archivo = Archivo('alumnos.txt')
        archivo.agregar_alumno(alumnos)

    archivo.mostrar_archivo()