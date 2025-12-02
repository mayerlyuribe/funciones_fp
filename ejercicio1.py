lista  = [1000, 0.01, 0.62, 20, 0.05, 1, 3847.10, 0.00026, 0.45, 17987539.67 ]

print("""
0. Kilómetro a metro
1. Centímetro a metro
2. Kilómetro por hora a millas por hora
3. Nota en Educatic a nota en Canvas
4. Nota en Canvas a nota en Educatic
5. Mililitro a centímetro cúbico
6. Dólar (USA) a peso colombiano
7. Peso colombiano a dólar (USA)
8. Libra a kilogramo
9. Minuto luz a kilómetro
""")

def conversion(opcion, valor):
    if opcion >=0 and opcion <=9:
        resultado = valor * lista[opcion]
        return resultado
    else:
        return None

while(True):
    opcion = int(input("ingrese la opción de la conversión que desea realizar: "))
    valor = float(input("ingrese el valor a convertir: "))
    resultado = conversion(opcion, valor)
    print("el resultado de la conversión es:", resultado)

    rta = input("desea realizar otra conversión? (si/no): ")
    if rta.lower() == "si":
        continue
    elif rta.lower() == "no":
        print("saliendo...")
        break;
    else:
        print("respuesta no válida, saliendo...")
        break