import os
import datetime
import time
import calendar
from tqdm import tqdm

# Constantes
fechaActual = datetime.datetime.now()

# Lista de estaciones disponibles
estaciones = ["Alajuela", "Heredia", "SJN (Sto Domingo)", "Cartago",
        "SJO (Alajuelita)", "Perez Zeledon", "San Carlos", "Puntarenas", 
        "Guapiles", "Nicoya", "Movil Sur", "Movil 4", "Liberia", "Cañas", 
        "Movil Norte", "Movil Central"]

# Diccionario de Vehiculos con sus respectivos costos
vehiculos = {"Motocicleta":8010, "Automóvil":12150, "Carga Liviana":12150, 
        "Carga Pesada":16015, "Bus":16015, "Taxi":13025}
        
class Persona:
    def __init__(self, nombre = None, apellidos = None, cedula = None,
        correo = None, telefono = None):
        self.nombre = nombre
        self.apellidos = apellidos
        self.cedula = correo
        self.correo = cedula
        self.telefono = telefono

class Cita(Persona):
    def __init__(self, placa = None, fecha = None, hora = None,
        estacion = None, vehiculo = None, monto = None):
        super().__init__()
        self.placa = placa
        self.fecha = fecha
        self.hora = hora
        self.estacion = estacion
        self.vehiculo = vehiculo
        self.monto = monto
       

    # Metodo para mostrar la lista estaciones.
    def mostrar_estaciones(self):
        os.system("cls")
        print("Estaciones: ")
        for i in range(len(estaciones)):
            print(f"{i + 1}- {estaciones[i]}")

    
    # Metodo para elegir la estacion de la lista estaciones.
    def elegir_estacion(self):
        try:
            opc = int(input("Ingrese el número de estación: "))
            self.estacion = estaciones[opc-1]
        except:
            opc = -1


    # Metodo que muestra los datos de los tipos de vehiculos y sus costos
    def mostrar_vehiculosYcostos(self):
        os.system("cls")
        print("Vehículos:")   
        # Imprimimos las key(Vehiculos) con sus valores(costo)
        for vehiculo, costo in vehiculos.items():
            print(f"{vehiculo} = c{costo}")


    def elegir_fecha(self):
        print("Ingrese la fecha de la cita: ")
        anio = fechaActual.year
        print(f"Año: {anio}")
        mes = input("Mes: ")
        dia = input("Día: ")
        return f"{anio}/{mes}/{dia}"

    def elegir_hora(self):
        horas = ["8:00am","9:00am","10:00am","11:00am","12:00pm",
        "1:00pm","2:00pm","3:00pm","4:00pm","5:00pm","6:00pm"]
        for i in range(len(horas)):
            print(f"{i}- {horas[i]}")        
        opc = int(input("Opcion: "))
        hora = horas[opc-1]
        return str(hora)
    
    # Metodo para crear una cita
    def nueva_cita(self):
        self.nombre = input("Nombre: ")
        self.apellidos = input("Apellidos: ")
        self.cedula = input("Cédula: ")
        self.placa = input("Placa Vehículo: ")
        self.fecha = self.elegir_fecha()
        self.hora = self.elegir_hora()
        self.mostrar_estaciones()
        self.elegir_estacion()
        os.system("cls")
        self.correo = input("Correo electrónico: ")
        self.telefono = input("Teléfono: ")
        
        while True:
            os.system("cls")
            ans = input(f"Yo, {self.nombre} con cédula: {self.cedula}, autorizo el \
uso del número celular y/o el correo electrónico a Riteve para el envío de información \
referente a la revisión téncnica vehícular.\n\nAcepta los términos? S = si | N = no : ")
            if ans == "S" or ans == "s":
                self.mostrar_vehiculosYcostos()
                print("\nPor favor ingrese el nombre del vehículo tal cual como sale en pantalla.\n")
                self.vehiculo = input("Vehículo: ")
                self.monto = vehiculos.get(str(self.vehiculo)) # Obtenemos valor de la key
                break
            else:
                os.system("cls")
                print(f"Debe aceptar los términos para continuar.")   
                input("'nPresione enter para continuar...")
        input("Presione enter para continuar...")


    def escribir_txt(self):
        with open("citas.txt", "a") as archivo:
            archivo.write(f"{self.cedula};{self.nombre};{self.apellidos};\
{self.placa};{self.fecha};{self.hora};{self.estacion};{self.correo};\
{self.telefono};{self.monto}\n")


    def mostrar_citas(self):
        with open("citas.txt", "r") as archivo:
            # Generamos una lista con las lineas del archivo con
            # el metodo readlines(),
            lineas = archivo.readlines()
            # Ordenamos la lista
            lineas.sort()
            linea = archivo.readline()
            cont = 0
            # Por cada linea en la lista lineas
            for linea in lineas:
                cont += 1
                # Creamos lista con el metodo split().
                atributos = linea.split(";")
                print(f"Cita #{cont}")
                print(f"Cédula: {atributos[0]}")
                print(f"Nombre: {atributos[1]}")
                print(f"Apellidos: {atributos[2]}")
                print(f"Placa: {atributos[3]}")
                print(f"Fecha: {atributos[4]}")
                print(f"Hora: {atributos[5]}")
                print(f"Estación: {atributos[6]}")
                print(f"Correo: {atributos[7]}")
                print(f"Monto: ₡{atributos[9]}")


     # Con el metodo de buscar empleado nos permitira buscar los empleados.
    def buscar_empleado(self):
        with open("citas.txt", "r") as file:
            # Asignamos el texto que tenga la linea a la variable line.
            line = file.readline()
            cedula = input("Cedula a buscar: ")
                # Validamos que la cedula no este vacia y que sean numeros.
            if cedula != "" and cedula.isnumeric():
                # Mientras la linea no este vacia nos va a recorrer las lineas del txt.
                while line != "":
                    '''Generaremos un array llamado atributos con los elementos
                    separados por ";".'''
                    atributos = line.split(";")
                    '''Si la cedula es igual al primer elemento del array atributos
                    (Que seria la cedula) entonces vamos a asignar los valores del 
                    array a los atributos del objeto para que no esten en "None"'''
                    if cedula == atributos[0]:
                        '''Luego podremos imprimir los atributos de lo que sera la
                        persona que buscamos con la cedula.'''
                        print(f"\nCedula: {atributos[0]}")
                        print(f"Nombre: {atributos[1]}")
                        print(f"Apellidos: {atributos[2]}")
                        print(f"Placa: {atributos[3]}")
                        print(f"Fecha: {atributos[4]}")
                        print(f"Hora: {atributos[5]}")
                        print(f"Estación: {atributos[6]}")
                        print(f"Correo: {atributos[7]}")
                        print(f"Monto: {atributos[9]}")
                    # Volvemos a llamar el metodo readline() que va a empezar a
                    # leer desde la otra linea.
                    line = file.readline()
            else:
                print("El número de cédula no se ha encontrado")


    # Metodo que nos permite modificar las citas
    def modificar_cita(self):
        with open('citas.txt', 'r') as file:
            data = file.readlines()
        print(data)
        data[1] = "Here is my modified Line 2\n"
        
        with open('citas.txt', 'w') as file:
            file.writelines(data)
    

    # Metodo para eliminar
    def eliminar_cita(self):
        with open("citas.txt", "r") as f:
            lines = f.readlines()
            ced = input("cedula a eliminar: ")
            for line in lines:
                atributos = line.split(';')
                if atributos[0] == ced:
                    toDelete = str(f"{atributos[0]};{atributos[1]};{atributos[2]};{atributos[3]};{atributos[4]};{atributos[5]};{atributos[6]};{atributos[7]};{atributos[8]};{atributos[9]}")
                    print(f"Cita encontrada.")
        with open("citas.txt", "w") as f:
            for line in lines:
                if line.strip("\n") != toDelete.strip("\n"):
                    f.write(line)
            print(f"La cita se ha eliminado correctamente.")
            
                    
    # Sobrecarga de operadores para acomodar las citas
    # por el nombre alfabeticamente
    def __lt__(self, obj):
        return self.nombre < obj.nombre

    def __eq__(self, obj):
        return self.nombre == obj.nombre

    def __le__(self, obj):
        return self < obj or self == obj
        

    # Metodo para imprimir el menu
    def menu(self):
        print("""1- Nueva Cita
2- Mostrar Citas
3- Buscar Cita
4- Modificar Citas
5- Eliminar Citas
6- Salir""")

def main():
    os.system("cls")
    print("Bienvenido al Sistema de Citas de Riteve!\n")

    # Barra de carga.
    for i in tqdm(range(10)):
        time.sleep(0.1)

    while True:       
        os.system("cls")
        print("==================")
        print("#     Riteve     #")
        print("==================\n")
        cita = Cita()
        cita.menu()

        try:
            opc = int(input("\nPor favor ingrese una opción: "))
        except:
            opc = -1       
        match opc:
            case 1:
                os.system("cls")
                print("*** Nueva Cita ***")    
                cita.nueva_cita()
                cita.escribir_txt()

            case 2:
                os.system("cls")
                print("*** Mostrar Citas ***\n")
                cita.mostrar_citas()
                input("\nPresione Enter para continuar...")

            case 3:
                os.system("cls")
                print("*** Buscar Cita ***\n")
                cita.buscar_empleado()
                input("\nPresione Enter para continuar...")

            case 4:
                os.system("cls")
                print("*** Modificar Citas ***")
                cita.modificar_cita()
                input("Presione Enter para continuar...")

            case 5:
                os.system("cls")
                print("*** Eliminar Citas ***")
                cita.eliminar_cita()
                input("Presione Enter para continuar...")

            case 6:
                print("Hasta luego!")
                time.sleep(1)
                break
            
            case _:
                print("Ingrese una opción valida.")
                input("Presione Enter para continuar...")
    
if __name__ == "__main__":
    main()