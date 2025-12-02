import math
times = int(input("Ingrese el número de veces que desea calcular la distancia entre dos puntos: "))

for i in range(times):
    print("Cálculo número ", i+1)
    x1 = int(input("ingrese la coordenada x del primer punto: "))
    y1 = int(input("ingrese la coordenada y del primer punto: "))
    print("------------------------------------------------")
    x2 = int(input("ingrese la coordenada x del segundo punto: "))
    y2 = int(input("ingrese la coordenada y del segundo punto: "))

    def distancia_puntos(x1, y1, x2, y2):
        return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    distancia = distancia_puntos(x1, y1, x2, y2)
    distancia_formateada = f"{distancia:,.2f}"
    print("la distancia entre los dos puntos es: ", distancia_formateada)