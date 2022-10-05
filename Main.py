#Importamos librerias y clases
import os
import time
from Cita import Cita
from tqdm import tqdm
#Constantes

#Metodo para imprimir el menu
def menu():
    print("""1- Nueva Cita
2- Mostrar Citas
3- Modificar Citas
4- Eliminar Citas
5- Salir
""")

def main():
    os.system("cls")
    print("Bienvenido al Sistema de Citas de Riteve!\n")
    '''for i in range(10):
        time.sleep(2)'''

    #Barra de carga
    for i in tqdm(range(10)):
        time.sleep(0.1)

    while True:       
        os.system("cls")
        print("==================")
        print("#     Riteve     #")
        print("==================\n")
        menu()
        cita = Cita()
        try:
            opc = int(input("Por favor ingrese una opcion: "))
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
                cita.leer_txt()
                input("\nPresione Enter para continuar...")

            case 3:
                os.system("cls")
                print("*** Modificar Citas ***")
                cita.leer_txt()
                cita.modificar_cita()             
                input("Presione Enter para continuar...")

            case 4:
                os.system("cls")
                print("*** Eliminar Citas ***")
                cita.eliminar_cita("Brandon")
                input("Presione Enter para continuar...")

            case 5:
                print("Saliendo...")
                time.sleep(1)
                break
            
            case _:
                print("Ingrese una opción valida.")
                input("Presione Enter para continuar...")
    
if __name__ == "__main__":
    main()