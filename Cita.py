# Bibliotecas
import os
import datetime
import time
import calendar

# Constantes
fechaActual = datetime.datetime.now()

#Lista de estaciones disponibles
estaciones = ["Alajuela", "Heredia", "SJN (Sto Domingo)", "Cartago",
        "SJO (Alajuelita)", "Perez Zeledon", "San Carlos", "Puntarenas", 
        "Guapiles", "Nicoya", "Movil Sur", "Movil 4", "Liberia", "Cañas", 
        "Movil Norte", "Movil Central"]

# Diccionario de Vehiculos con sus respectivos costos
vehiculos = {"Motocicleta":8010, "Automovil":12150, "Carga Liviana":12150, 
        "Carga Pesada":16015, "Bus":16015, "Taxi":13025}
        

class Cita:
    # Constructor
    def __init__(self, nombre=None, apellidos=None, cedula=None, placa=None, 
    fecha=None, hora=None, estacion=None, correo=None, telefono=None, 
    vehiculo=None, monto=None):
        # Trabajamos los atributos como privados
        self._nombre = nombre
        self._apellidos = apellidos
        self._cedula = cedula
        self._placa = placa
        self._fecha = fecha
        self._hora = hora
        self._estacion = estacion
        self._correo = correo
        self._telefono = telefono
        self._vehiculo = vehiculo
        self._monto = monto
        
    # Propiedades de los atributos:
    @property #Getter
    def nombre(self):
        return self._nombre    
    @nombre.setter #Setter
    def nombre(self, valor):
        self._nombre = valor    
    @nombre.deleter #Deleter
    def nombre(self):
        del self._nombre
    
    @property #Getter
    def apellidos(self):
        return self._apellidos    
    @apellidos.setter #Setter
    def apellidos(self, valor):
        self._apellidos = valor    
    @apellidos.deleter #Deleter
    def apellidos(self):
        del self._apellidos

    @property #Getter
    def placa(self):
        return self._placa   
    @placa.setter #Setter
    def placa(self, valor):
        self._placa = valor    
    @placa.deleter #Deleter
    def placa(self):
        del self._placa

    @property #Getter
    def fecha(self):
        return self._fecha  
    @fecha.setter #Setter
    def fecha(self, valor):
        self._fecha = valor    
    @fecha.deleter #Deleter
    def fecha(self):
        del self._fecha

    @property #Getter
    def hora(self):
        return self._hora
    @hora.setter #Setter
    def hora(self, valor):
        self._hora = valor    
    @hora.deleter #Deleter
    def hora(self):
        del self._hora

    @property #Getter
    def estacion(self):
        return self._estacion    
    @estacion.setter #Setter
    def estacion(self, valor):
        self._estacion = valor    
    @estacion.deleter #Deleter
    def estacion(self):
        del self._estacion

    @property #Getter
    def correo(self):
        return self._correo  
    @correo.setter #Setter
    def correo(self, valor):
        self._correo = valor    
    @correo.deleter #Deleter
    def correo(self):
        del self._correo

    @property #Getter
    def telefono(self):
        return self._telefono 
    @telefono.setter #Setter
    def telefono(self, valor):
        self._telefono = valor    
    @telefono.deleter #Deleter
    def telefono(self):
        del self._telefono

    @property #Getter
    def cedula(self):
        return self._cedula
    @cedula.setter #Setter
    def cedula(self, valor):
        self._cedula = valor    
    @cedula.deleter #Deleter
    def cedula(self):
        del self._cedula

    @property #Getter
    def vehiculo(self):
        return self._vehiculo
    @vehiculo.setter #Setter
    def vehiculo(self, valor):
        self._vehiculo = valor    
    @vehiculo.deleter #Deleter
    def vehiculo(self):
        del self._vehiculo
    
    @property #Getter
    def monto(self):
        return self._monto
    @monto.setter #Setter
    def monto(self, valor):
        self._monto = valor    
    @monto.deleter #Deleter
    def monto(self):
        del self._monto


    #Metodo para mostrar la lista estaciones.
    def mostrar_estaciones(self):
        os.system("cls")
        print("Estaciones: ")
        for i in range(len(estaciones)):
            print(f"{i + 1}- {estaciones[i]}")

    
    #Metodo para elegir la estacion de la lista estaciones.
    def elegir_estacion(self):
        try:
            opc = int(input("Ingrese el numero de estación: "))
            self.estacion = estaciones[opc-1]
        except:
            opc = -1


    #Metodo que muestra los datos de los tipos de vehiculos y sus costos
    def mostrar_vehiculosYcostos(self):
        os.system("cls")
        print("Vehículos:")
        # Imprimimos las key(Vehiculos) con sus valores(costo)
        for vehiculo, costo in vehiculos.items():
            print(f"{vehiculo} = c{costo}")
    
    #Metodo que muestra el calendario
    def mostrar_calendario(self):
        c = calendar.TextCalendar(calendar.MONDAY)
        str = c.formatmonth(2022,10)
        print(str)

    
    #Metodo para crear una cita
    def nueva_cita(self):
        self.nombre = input("Nombre: ")
        self.apellidos = input("Apellidos: ")
        self.cedula = input("Cédula: ")
        self.placa = input("Placa Vehículo: ")
        self.mostrar_calendario()
        self.fecha = datetime.datetime.now().date()
        self.hora = datetime.datetime.strftime(fechaActual,"%H:%M:%S")
        self.mostrar_estaciones()
        self.elegir_estacion()
        self.correo = input("Correo electrónico: ")
        self.telefono = input("Teléfono: ")
        
        while True:
            ans = input(f"Yo, {self.nombre} con cédula: {self.cedula}, autorizo el uso del número celular y/o el correo electrónico a Riteve para el envío de información referente a la revision téncnica vehícular.\n Acepta los términos? S = si | N = no : ")
            if ans == "S" or ans == "s":
                self.mostrar_vehiculosYcostos()
                print("\nPor favor ingrese el nombre del vehículo tal cual como sale en pantalla.\n")
                self.vehiculo = input("Vehículo: ")
                self.monto = vehiculos.get(str(self.vehiculo)) #Obtenemos valor de la key
                break
            else:
                os.system("cls")
                print(f"Debe aceptar los terminos para continuar.")   
                time.sleep(1.4) 
        input("Presione enter para continuar...")

    def escribir_txt(self):
        with open("citas.txt", "a") as archivo:
            archivo.write(f"{self.nombre};{self.apellidos};{self.cedula};{self.placa};{self.fecha};{self.hora};{self.estacion};{self.correo};{self.telefono};{self.monto}\n")

    def leer_txt(self):
        cont = 1
        with open("citas.txt", "r") as archivo:
            #Readlines nos genera una lista con las lineas del archivo
            lineas = archivo.readlines()
            linea = archivo.readline()
            #Por cada linea en la lista lineas
            for linea in lineas:
                '''El metodo split nos genera un array con el separador
                que le mandemos por parametro, en este caso ";"'''
                atributos = linea.split(";")
                cont = 1
                print(f"""Cita #
Nombre: {atributos[0]}
Apellidos: {atributos[1]}
Cedula: {atributos[2]}
Placa: {atributos[3]}
Fecha: {atributos[4]}
Hora: {atributos[5]}
Estacion: {atributos[6]}
Correo: {atributos[7]}
Telefono: {atributos[8]}
Monto: {atributos[9]}""")


    #Metodo  que nos permite modificar las citas
    def modificar_cita(self, palabra):
        with open("citas.txt", "r") as archivo:
            # Variables auxiliares para obtener la posicion del cursor
            # y asi poder trabajar con los datos que nosotros queramos.
            i = 1
            enc = 0
            poscamb = 0
            pospuntero = 0
            linea = archivo.readline()
            tamLin = len(linea)
            tamNombre = len(palabra)
            while linea != "" and enc == "":
                if linea[1:1+tamNombre+1] == palabra+";":
                    poscamb = archivo.tell()
                    enc = 1 
                    pospuntero = poscamb - tamLin -1
                else:
                    i += 1
                    linea = archivo.readline()
            
            if enc == 0:
                print("El dato ingresado no se encuentra")
            if enc == 1:
                with open("citas.txt", "r+") as archivo2:
                    if pospuntero == 1:
                        archivo2.seek(0)
                    else:
                        archivo2.seek(pospuntero)
                    for n in range(0, tamLin, 1):
                        archivo2.write("")

    #Metodo que busca el dato a eliminar y lo elimina
    def eliminar_cita(self, palabra):
        with open("citas.txt", "r") as archivo:
            # Variables auxiliares para obtener la posicion del cursor
            # y asi poder trabajar con los datos que nosotros queramos.
            i = 1
            enc = 0
            poscamb = 0
            pospuntero = 0
            linea = archivo.readline()
            tamLin = len(linea)
            tamNombre = len(palabra)
            while linea != "" and enc == "":
                if linea[1:1 + tamNombre + 1] == palabra + ";":
                    poscamb = archivo.tell()
                    enc = 1
                    pospuntero = poscamb - tamLin -1
                else:
                    i += 1
                    linea = archivo.readline()
            
            if enc == 0:
                print("El dato ingresado no se encuentra")
            if enc == 1:

                with open("citas.txt", "r+") as archivo2:
                    # Al ya posicionar el cursor donde corresponda el txt
                    # Procedemos a reemplazar el dato por ""
                    if pospuntero == 1:
                        archivo2.seek(0)
                    else:
                        archivo2.seek(pospuntero)
                    for n in range(0, tamLin, 1):
                        archivo2.write("")