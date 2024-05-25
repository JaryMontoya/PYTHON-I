
#crear un programa para gestionar una lista de contactos, cada contacto debe tener un nombre y un número de teléfono"
#1. Permitir agregar nuevos contactos
#2. Mostrar todos los contactos
#3. Buscar un contacto por nombre
#4. Eliminar un contacto
#5. Permitir al usuario realizar otra operacion
def agregar_contacto(contactos):
    nombre = input("Introduce el nombre del contacto: ")
    telefono = input("Introduce el número de teléfono del contacto: ")
    if nombre in contactos:
        print("El contacto ya existe.")
    else:
        contactos[nombre] = telefono
        print("Contacto agregado exitosamente.")

def mostrar_contactos(contactos):
    if not contactos:
        print("No hay contactos para mostrar.")
    else:
        for nombre, telefono in contactos.items():
            print(f"Nombre: {nombre}, Teléfono: {telefono}")

def buscar_contacto(contactos):
    nombre = input("Introduce el nombre del contacto que deseas buscar: ")
    if nombre in contactos:
        print(f"Teléfono de {nombre}: {contactos[nombre]}")
    else:
        print("El contacto no existe.")

def eliminar_contacto(contactos):
    nombre = input("Introduce el nombre del contacto que deseas eliminar: ")
    if nombre in contactos:
        del contactos[nombre]
        print("Contacto eliminado exitosamente.")
    else:
        print("El contacto no existe.")

def gestionar_contactos():
    contactos = {}
    while True:
        print("\nGestión de Contactos")
        print("1. Agregar nuevo contacto")
        print("2. Mostrar todos los contactos")
        print("3. Buscar un contacto por nombre")
        print("4. Eliminar un contacto")
        print("5. Salir")

        opcion = input("Introduce el número de la operación que deseas realizar: ")

        if opcion == '1':
            agregar_contacto(contactos)
        elif opcion == '2':
            mostrar_contactos(contactos)
        elif opcion == '3':
            buscar_contacto(contactos)
        elif opcion == '4':
            eliminar_contacto(contactos)
        elif opcion == '5':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, selecciona una opción válida.")

# Ejecutar la gestión de contactos
gestionar_contactos()
