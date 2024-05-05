tareas = []

def sumar_tarea(nombre, descripcion, dificultad):
    tareas.append({"Nombre": nombre, "Descripcion": descripcion, "Dificultad": dificultad})

def eliminar_tarea(nombre):
    for i in tareas:
        if i["Nombre"] == nombre:
            tareas.remove(i)

def modificar_tarea(nombre, valor):
    for i in tareas:
        if i["Nombre"] == nombre:
            i["Nombre"] = valor

def mostrar_tareas(dif):
    for i in tareas:
        if i["Dificultad"] == dif:
            print(i)

def mostrar_todas():
    print(tareas)

respuesta = "nada"

while respuesta != 0:
    respuesta = int(input("Seleccione el numero que desee: \n 0. Finalizar Programa \n 1. Sumar Tarea \n 2. Eliminar Tarea \n 3. Modificar tarea \n 4. Mostrar Tarea \n 5. Mostrar todas las tareas \n"))
    if respuesta == 1:
        nombre = input("Ingrese el nombre de la tarea que quiera sumar: ")
        descripcion = input("Ingrese la descripcion de la tarea que quiera sumar: ")
        dificultad = input("Ingrese la dificultad de la tarea que quiera sumar: ")
        sumar_tarea(nombre, descripcion, dificultad)
        mostrar_todas()
    if respuesta == 2:
        nombre = input("Ingrese el nombre de la tarea que quiera eliminar: ")
        eliminar_tarea(nombre)
        mostrar_todas()
    if respuesta == 3:
        nombre = input("Ingrese el nombre de la tarea que quiera modificar: ")
        valor = input("Ingrese el nuevo valor: ")
        modificar_tarea(nombre, valor)
        mostrar_todas()
    if respuesta == 4:
        dif = input("Ingrese la dificultad de la tarea que quiera ver: ")
        mostrar_tareas(dif)
    if respuesta == 5:
        mostrar_todas()