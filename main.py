from sumar import sumar
from resta import restar
from multiplicacion import multiplicar
from dividir import dividir
from suma_avanzada import suma_avanzada

def menu():
    while True:  # Bucle para que el menú se repita hasta que el usuario elija salir
        print("Calculadora:")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Suma avanzada")
        print("0. Salir")

        opcion = int(input("Selecciona una opción: "))
        
        if opcion == 1:
            a, b = map(float, input("Ingresa dos números separados por un espacio: ").split())
            print(f"Resultado: {sumar(a, b)}")
        elif opcion == 2:
            a, b = map(float, input("Ingresa dos números separados por un espacio: ").split())
            print(f"Resultado: {restar(a, b)}")
        elif opcion == 3:
            a, b = map(float, input("Ingresa dos números separados por un espacio: ").split())
            print(f"Resultado: {multiplicar(a, b)}")
        elif opcion == 4:
            a, b = map(float, input("Ingresa dos números separados por un espacio: ").split())
            print(f"Resultado: {dividir(a, b)}")
        elif opcion == 5:
            numeros = list(map(float, input("Ingresa números separados por espacios: ").split()))
            print(f"Resultado: {suma_avanzada(numeros)}")
        elif opcion == 0:
            print("¡Adiós!")
            break  # Salir del bucle
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")

if __name__ == "__main__":
    menu()
