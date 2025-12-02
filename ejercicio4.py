print("-- hello docente --")
diccionario = {}

est = int(input("Ingrese la cantidad de alumnos a los que va a evaluar: "))
tareas = int(input("Ingrese la cantidad de tareas que se van a calificar: "))

for i in range(tareas):
    name = input(f"ingrese el nombre de la tarea {i + 1}: ")
    ponderacion = float(input(f"ingrese la ponderacion de la tarea {i + 1} (%): "))
    diccionario[name] = ponderacion

print(diccionario)

def evalua_alumno(ponderacion, nota):
    nota_final += (ponderacion * nota) / 100
    ponderacion_total += ponderacion
    return nota_final, ponderacion_total

print(evalua_alumno(ponderacion, 59))

