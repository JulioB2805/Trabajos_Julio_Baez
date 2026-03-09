#Leer por teclado dos numeros e imprimir el mayor o si ambos son iguales

print("---Bienvenido----")
num1=int(input("Ingrese su primer numero: "))
num2=int(input("Ingrese su segundo numero: "))

print(f"Los numeros ingresados fueron:{num1} y {num2}")

if num1==num2:
    print("Los numeros son iguales...")
elif num1>num2:
    print(f"El mayor de ellos es {num1}")
else:
    print(f"El mayor de ellos es {num2}")