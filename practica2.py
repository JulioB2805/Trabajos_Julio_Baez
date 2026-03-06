""" Escriba un programa para validar si los datos de acceso(usuario y contraseña) se encuentren en el diccionario.
Validar a solo 3 intentos erroneos de contraseña utilizando ciclo while. """
datos_acceso={"camila1984":12345,"Juan12":00000,"Hector@54":1590}
intentos_contraseña=0

while intentos_contraseña<=3:
 
   contraseña=int(input("Ingrese su contraseña para acceder: "))
   if contraseña not in (12345, 0, 1590):
    print("Contraseña Incorrecta,intentelo de nuevo.")
    intentos_contraseña=intentos_contraseña + 1
   elif contraseña==12345:
    print("Bienvenida Camila1984")
   elif contraseña==00000:
    print("Bienvenido Juan12")
   elif contraseña==1590:
    print("Bienvenido Hector@54")
   else:
    print("Error,usuario no valido")
print("Usuario bloqueado temporalmente")