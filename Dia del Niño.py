def preparar_datos(info):
    # Ahora funciona correctamente con cadenas (como se usa en iniciar())
    acumulador = ""
    for letra in info:
        acumulador += letra + "-"
    return acumulador[:-1]

def mezcla_datos(a, b):
    # Compara las cadenas resultantes
    if a > b:
        return a + b
    elif a == b:
        return a * 2  # Aunque multiplicar cadenas no es lo más común
    else:
        return b + a

def iniciar():
    entrada1 = input("Ingresa un valor de referencia textual: ")
    entrada2 = input("Ingresa otra unidad: ")
    x = preparar_datos(entrada1)
    y = preparar_datos(entrada2)
    resultado = mezcla_datos(x,  y)
    print("Resultado no final: ", resultado)
    # Ahora la impresión de "Coincidencia detectada." está dentro del bloque if
    if entrada1 in entrada2:
        print("Coincidencia detectada.")

iniciar()