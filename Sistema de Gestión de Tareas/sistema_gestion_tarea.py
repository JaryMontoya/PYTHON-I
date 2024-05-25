""" Desarrolla un sistema de gestión de tareas que permita al usuario añadir, ver, buscar,
actualizar y eliminar tareas. Cada tarea debe tener un título, una descripción y un estado
(pendiente o completada). El programa debe:
1. Permitir agregar nuevas tareas: Utiliza una clase Tarea para almacenar los detalles de
cada tarea y guarda los objetos en una lista.
2. Mostrar todas las tareas: Recorre la lista y muestra los detalles de cada tarea.
3. Buscar una tarea por título: Permite encontrar y mostrar información de una tarea
específica.
4. Actualizar el estado de una tarea: Permite cambiar el estado de una tarea a
"completada".
5. Eliminar una tarea por título: Permite remover una tarea de la lista.
6. Manejar posibles errores (como ingresar datos no válidos): Utiliza bloques try-except
para manejar errores en las entradas.
7. Permitir al usuario realizar otra operación o salir del programa: Un bucle while permite
repetir el proceso hasta que el usuario decida salir. """


class Tarea:
    def __init__(self, titulo, descripcion, estado="pendiente"):
        self.titulo = titulo
        self.descripcion = descripcion
        self.estado = estado

    def __str__(self):
        return f"Título: {self.titulo}\nDescripción: {self.descripcion}\nEstado: {self.estado}"


def agregar_tarea(tareas):
    try:
        titulo = input("Introduce el título de la tarea: ")
        descripcion = input("Introduce la descripción de la tarea: ")
        tarea = Tarea(titulo, descripcion)
        tareas.append(tarea)
        print("Tarea agregada exitosamente.")
    except Exception as e:
        print(f"Error al agregar la tarea: {e}")


def mostrar_todas_las_tareas(tareas):
    if not tareas:
        print("No hay tareas para mostrar.")
    else:
        for tarea in tareas:
            print(tarea)
            print("-" * 20)


def buscar_tarea_por_titulo(tareas):
    try:
        titulo = input("Introduce el título de la tarea que deseas buscar: ")
        for tarea in tareas:
            if tarea.titulo == titulo:
                print(tarea)
                return
        print("Tarea no encontrada.")
    except Exception as e:
        print(f"Error al buscar la tarea: {e}")


def actualizar_estado_tarea(tareas):
    try:
        titulo = input("Introduce el título de la tarea que deseas actualizar: ")
        for tarea in tareas:
            if tarea.titulo == titulo:
                tarea.estado = "completada"
                print("Estado de la tarea actualizado a 'completada'.")
                return
        print("Tarea no encontrada.")
    except Exception as e:
        print(f"Error al actualizar la tarea: {e}")


def eliminar_tarea(tareas):
    try:
        titulo = input("Introduce el título de la tarea que deseas eliminar: ")
        for tarea in tareas:
            if tarea.titulo == titulo:
                tareas.remove(tarea)
                print("Tarea eliminada exitosamente.")
                return
        print("Tarea no encontrada.")
    except Exception as e:
        print(f"Error al eliminar la tarea: {e}")


def gestionar_tareas():
    tareas = []
    while True:
        print("\nGestión de Tareas")
        print("1. Agregar nueva tarea")
        print("2. Mostrar todas las tareas")
        print("3. Buscar una tarea por título")
        print("4. Actualizar el estado de una tarea")
        print("5. Eliminar una tarea")
        print("6. Salir")

        try:
            opcion = int(input("Introduce el número de la operación que deseas realizar: "))

            if opcion == 1:
                agregar_tarea(tareas)
            elif opcion == 2:
                mostrar_todas_las_tareas(tareas)
            elif opcion == 3:
                buscar_tarea_por_titulo(tareas)
            elif opcion == 4:
                actualizar_estado_tarea(tareas)
            elif opcion == 5:
                eliminar_tarea(tareas)
            elif opcion == 6:
                print("Saliendo del programa.")
                break
            else:
                print("Opción no válida. Por favor, selecciona una opción válida.")
        except ValueError:
            print("Entrada no válida. Por favor, introduce un número.")
        except Exception as e:
            print(f"Ha ocurrido un error: {e}")


# Ejecutar la gestión de tareas
gestionar_tareas()
