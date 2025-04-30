numero = int(input("Ingrese el primer número: "))
if numero % 2 == 0:
    print ("El numero es par.")
else:
    print ("El numero es impar.")

cantidad = int(input("Cuantos numeros pares desea ver?:"))
contador= 0
i = 1

while cantidad > contador :
   if i % 2 == 0:
        print ("Par numero", contador + 1, ":",i)
        contador += 1
        i += 1