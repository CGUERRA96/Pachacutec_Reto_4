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
            alumno = f'{alumno.dni}, {alumno.nombre}, {alumno.edad}, {alumno.nota}, {alumno.notami}, {alumno.notamax}, {alumno.notaprom}\n'
            file.write(alumno)
        except Exception as e:
            print(f'{str(e)}')
        finally:
            if(file):
                file.close()
                print('Se visualiza un alumno')


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


cant_alumnos = int(input('Cuantos alumnos se agregara?: '))

lista_alumnos = []
for a in range(cant_alumnos):
    alumno_nombre = []
    alumnos_nombre = input('Como te llamas?: ')
    alumno_dni = []
    alumnos_dni = input('Cual es tu dni?: ')
    alumno_edad = []
    alumnos_edad = int(input('Cual es tu edad: '))

    cant_notas = int(input('Ingrese cantidad de notas: '))
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
        'alumno': {
            'nombre': alumnos_nombre,
            'DNI': alumnos_dni,
            'Edad': alumnos_edad
        },
        'notas': lista_nota
    })

for v in lista_alumnos:
    print("########################")
    print(f"Alumnos : {v['alumno']['nombre']}")
    print(f"Alumnos : {v['alumno']['DNI']}")
    print(f"Alumnos : {v['alumno']['Edad']}")    
    print(f"notas: {v['notas']}")
    print(lista_alumnos)
                  
alumnos = Alumno(alumnos_nombre, alumnos_dni, alumnos_edad, lista_nota, f"{min(v['notas'])}", f"{max(v['notas'])}", f"{sum(v['notas'])/len(v['notas'])}")
archivo = Archivo('alumnos.txt')
archivo.agregar_alumno(alumnos)

#archivo.mostrar_archivo()