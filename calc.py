import os

def suma_impares(rango):
    suma = 0
    for i in range(rango + 1):
        if i % 2 != 0:
            suma += i
    return suma

def main():
    os.system("cls")
    num = int(input("Ingrese numero: "))
    print(f"La suma de los numeros impares hasta el {num} es: {suma_impares(num)}")

if __name__ == "__main__":
    main()