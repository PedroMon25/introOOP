class Alumno:
    # Constructor con atributos vacíos
    def __init__(self):
        #Atributos privados
        self.__nombre = None
        self.__apellido_paterno = None
        self.__apellido_materno = None
        self.__no_control = None
        self.__semestre = None

    # Métodos setters
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_apellido_paterno(self, apellido_paterno):
        self.__apellido_paterno = apellido_paterno

    def set_apellido_materno(self, apellido_materno):
        self.__apellido_materno = apellido_materno

    def set_no_control(self, no_control):
        self.__no_control = no_control

    def set_semestre(self, semestre):
        self.__semestre = semestre

    # Métodos getters
    def get_nombre(self):
        return self.__nombre

    def get_apellido_paterno(self):
        return self.__apellido_paterno

    def get_apellido_materno(self):
        return self.__apellido_materno

    def get_no_control(self):
        return self.__no_control

    def get_semestre(self):
        return self.__semestre

    def get_nombre_completo(self):
        return f"{self.__nombre} {self.__apellido_paterno} {self.__apellido_materno}"

# Diccionario para almacenar los alumnos
registro_alumnos = {}

# Capturar 3 registros
for i in range(3):
    alumno = Alumno()  # Crear una nueva instancia para cada alumno
    alumno.set_nombre(input("Introduce el nombre: "))
    alumno.set_apellido_paterno(input("Introduce el apellido paterno: "))
    alumno.set_apellido_materno(input("Introduce el apellido materno: "))
    alumno.set_no_control(input("Introduce el número de control: "))
    alumno.set_semestre(int(input("Introduce el semestre: ")))

    registro_alumnos[i] = alumno  # Almacenar la instancia en el diccionario

# Mostrar los 3 nombres de los registros
for i in range(3):
    print(f"Nombre del alumno {i+1}: {registro_alumnos[i].get_nombre_completo()}")
