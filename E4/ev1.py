# Ingresar el sueldo de una persona,si supera los 80.000.000 millones anuales mostrar un
# mensaje en pantalla indicando que debe abonar IRP
# sino mostrar el mensaje la persona No debe abonar impuestos
print("---Bienvenido---")
Datos_n= input("Ingrese su nombre: ") #añadido para más interacción
Datos_c= float(input("Ingrese su numero de telefono: "))  #añadido para más interacción

MONTOIRP = 80000000
sueldo_mes = int (input("Ingrese el monto de su sueldo mensual: "))
sueldo_anual = sueldo_mes * 12

if sueldo_anual == MONTOIRP:
    print(f"{Datos_n},Estas en el limite, tu sueldo es 80.000.000")
elif sueldo_anual > MONTOIRP:
    print(f"Atención {Datos_n}, tienes que pagar impuesto...")
else:
    print(f"{Datos_n},No debes de abonar nada.")