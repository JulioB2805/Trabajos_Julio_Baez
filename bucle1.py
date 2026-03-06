#programa para validar los datos de acceso ingresados por teclado por el usuario.
#Los datos leídos son user y password
user="admin"
password=12345
user=input("Ingrese su usuario: ")
password=int(input("Ingrese su contraseña: "))
if user=="admin" and password==12345:
    print("Acceso correcto.")
else:
    print("Acceso denegado.")
