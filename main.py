num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
operacion = input("Seleccione una operación (+, -, *, /): ")

if operacion == '+':
    resultado = num1 + num2
    print(f"Resultado: {resultado:.2f}")
elif operacion == '-':
    resultado = num1 - num2
    print(f"Resultado: {resultado:.2f}")
elif operacion == '*':
    resultado = num1 * num2
    print(f"Resultado: {resultado:.2f}")
elif operacion == '/':
    if num2 != 0:
        resultado = num1 / num2
        print(f"Resultado: {resultado:.2f}")
    else:
        print("Error: No se puede dividir entre cero.")
else:
    print("Operación no válida.")