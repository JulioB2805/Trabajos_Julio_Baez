import math

def circulo():
    radio = float(input("Ingrese el radio del círculo: "))
    area = math.pi * radio ** 2
    perimetro = 2 * math.pi * radio
    print(f"Área del círculo: {area:}")
    print(f"Perímetro del círculo: {perimetro:}")

def rectangulo():
    base = float(input("Ingrese la base del rectángulo: "))
    altura = float(input("Ingrese la altura del rectángulo: "))
    area = base * altura
    perimetro = 2 * (base + altura)
    print(f"Área del rectángulo: {area:}")
    print(f"Perímetro del rectángulo: {perimetro:}")

def triangulo():
    lado1 = float(input("Ingrese el primer lado del triángulo: "))
    lado2 = float(input("Ingrese el segundo lado del triángulo: "))
    lado3 = float(input("Ingrese el tercer lado del triángulo: "))
    altura = float(input("Ingrese la altura correspondiente a la base (lado1): "))
    
    area = (lado1 * altura) / 2
    perimetro = lado1 + lado2 + lado3
    
    print(f"Área del triángulo: {area:}")
    print(f"Perímetro del triángulo: {perimetro:}")

while True:
    print("\n--- MENÚ ---")
    print("1. Círculo")
    print("2. Rectángulo")
    print("3. Triángulo") 
    print("4. Salir")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        circulo()
    elif opcion == "2":
        rectangulo()
    elif opcion == "3":
        triangulo()
    elif opcion == "4":
        print("Programa finalizado.")
        break
    else:
        print("Opción inválida, intente nuevamente.")
