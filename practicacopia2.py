datos_acceso = {"camila1984": 12345, 
                "Juan12": 0, 
                "Hector@54": 1590}

intentos = 0
acceso_concedido = False

while intentos < 3 and not acceso_concedido:
    usuario = input("Ingrese su usuario: ")
    contraseña = int(input("Ingrese su contraseña: "))

    if usuario in datos_acceso:
        if datos_acceso[usuario] == contraseña:
            print("Bienvenido/a", usuario)
            acceso_concedido = True
        else:
            print("Contraseña incorrecta.")
            intentos += 1
    else:
        print("Usuario no existe.")
        intentos += 1

if not acceso_concedido:
    print("Usuario bloqueado temporalmente.")