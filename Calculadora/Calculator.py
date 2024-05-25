def suma(a, b):
    return a + b


def resta(a, b):
    return a - b


def multiplicacion(a, b):
    return a * b


def division(a, b):
    if b == 0:
        return "Error: División por cero"
    return a / b


def calculadora():
    print("Calculadora Básica en Python")
    print("Selecciona una operación:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")

    operacion = input("Introduce el número de la operación (1/2/3/4): ")

    if operacion in ['1', '2', '3', '4']:
        num1 = float(input("Introduce el primer número: "))
        num2 = float(input("Introduce el segundo número: "))

        if operacion == '1':
            print(f"{num1} + {num2} = {suma(num1, num2)}")
        elif operacion == '2':
            print(f"{num1} - {num2} = {resta(num1, num2)}")
        elif operacion == '3':
            print(f"{num1} * {num2} = {multiplicacion(num1, num2)}")
        elif operacion == '4':
            print(f"{num1} / {num2} = {division(num1, num2)}")
    else:
        print("Operación no válida. Por favor, selecciona una operación válida.")


# Ejecutar la calculadora
calculadora()
