class Alumno:
    #Crea la funcion constructor con atributos vacios
    def __init__(self):
        # Atributos privados
        self.__nombre = None
        self.__apellido_paterno = None
        self.__apellido_materno = None
        self.__no_control = None
        self.__semestre = None

    # Métodos para agregar valores a los atributos
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

    # Métodos para obtener los valores almacenados en los atributos
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

registro_alumnos = {}

#Diccionario para almacenar los 50 alumnos

#Capturar 3 registros
for i in range(3):
    alumno = Alumno()
    alumno.set_nombre (input("Introduce el nombre:"))
    alumno.set_apellido_paterno (input("Introduce el apellido paterno:"))
    alumno.set_apellido_materno (input("Introduce el apellido materno:"))
    alumno.set_no_control (input("Introduce el numero de control:"))
    alumno.set_semestre (int(input("Introduce el semestre:")))

    registro_alumnos[i] = alumno

#Mostrar los 3 nombres de los registros
for i in range(3):
    print(f"Nombre del alumno{i+1}: {registro_alumnos[i].get_nombre_completo()}")

#Asignar valores usando los setters
# alumno.set_nombre("Carlos")
# alumno.set_apellido_paterno("Valle")
# alumno.set_apellido_materno("Suarez")
# alumno.set_no_control(123456789)
# alumno.set_semestre(5)

# #Obtener los valores usando getters
# print("Nombre:", alumno.get_nombre())
# print ("Apellido paterno:", alumno.get_apellido_paterno())
# print("Apellido materno:", alumno.get_apellido_materno())
# print("No.control:", alumno.get_no_control())
# print("Semestre:", alumno.get_semestre())
#
# print("Nombre_completo:", alumno.get_nombre_completo())
