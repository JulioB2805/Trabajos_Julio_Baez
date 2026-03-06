texto = input("Ingrese un texto: ")
mi_archivo = 'archivo-'+ texto + '.txt'
f = open (mi_archivo , 'w')# para apertura w= write, r = read , a = append
f.write(f'{texto}\n')
f.close()