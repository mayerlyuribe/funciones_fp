print("""
1. de Binario a Decimal
2. de Decimal a Binario
3. de Binario a Hexadecimal
4. de Hexadecimal a Binario
5. de Hexadecimal a Decimal
6. de Decimal a Hexadecimal""")

opcion = int(input("seleccione la opcion de conversión deseada (1-6): "))
num = input("ingrese el número a convertir: ")

def binario_a_decimal(bin_num):
    bin_str = str(bin_num)
    decimal = 0
    potencia = len(bin_str) - 1
    
    for digito in bin_str:
        decimal += int(digito) * (2 ** potencia)
        potencia -= 1
    
    return decimal

def decimal_a_binario(dec_num):
    if dec_num == 0:
        return "0"
    
    binario = ""
    while dec_num > 0:
        residuo = dec_num % 2
        binario = str(residuo) + binario
        dec_num //= 2
    
    return binario

def binario_a_hexadecimal(bin_num):
    decimal = binario_a_decimal(bin_num)
    hexa_nums = {
        0: "0", 1: "1", 2: "2", 3: "3",
        4: "4", 5: "5", 6: "6", 7: "7",
        8: "8", 9: "9", 10: "A", 11: "B",
        12: "C", 13: "D", 14: "E", 15: "F"
    }
    hexadecimal = hexa_nums[decimal]
    return hexadecimal

def hexadecimal_a_binario(hex_num):
    hexa_nums = {
        "0": 0, "1": 1, "2": 2, "3": 3,
        "4": 4, "5": 5, "6": 6, "7": 7,
        "8": 8, "9": 9, "A": 10, "B": 11,
        "C": 12, "D": 13, "E": 14, "F": 15
    }
    decimal = hexa_nums[hex_num.upper()]
    binario = decimal_a_binario(decimal)
    return binario

def hexadecimal_a_decimal(hex_num):
    hexa_nums = {
        "0": 0, "1": 1, "2": 2, "3": 3,
        "4": 4, "5": 5, "6": 6, "7": 7,
        "8": 8, "9": 9, "A": 10, "B": 11,
        "C": 12, "D": 13, "E": 14, "F": 15
    }
    decimal = hexa_nums[hex_num.upper()]
    return decimal

def decimal_a_hexadecimal(dec_num):
    hexa_nums = {
        0: "0", 1: "1", 2: "2", 3: "3",
        4: "4", 5: "5", 6: "6", 7: "7",
        8: "8", 9: "9", 10: "A", 11: "B",
        12: "C", 13: "D", 14: "E", 15: "F"
    }
    hexadecimal = hexa_nums[dec_num]
    return hexadecimal


if opcion == 1:
    resultado = binario_a_decimal(num)
    print(f"El número binario {num} en decimal es: {resultado}")
elif opcion == 2:
    resultado = decimal_a_binario(int(num))
    print(f"El número decimal {num} en binario es: {resultado}") 
elif opcion == 3:
    resultado = binario_a_hexadecimal(num)
    print(f"El número binario {num} en hexadecimal es: {resultado}")
elif opcion == 4:
    resultado = hexadecimal_a_binario(num)
    print(f"El número hexadecimal {num} en binario es: {resultado}")
elif opcion == 5:
    resultado = hexadecimal_a_decimal(num)
    print(f"El número hexadecimal {num} en decimal es: {resultado}")
elif opcion == 6:
    resultado = decimal_a_hexadecimal(int(num))
    print(f"El número decimal {num} en hexadecimal es: {resultado}")
else:
    print("Opción inválida.")