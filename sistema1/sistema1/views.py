from django.http import HttpResponse 

def saludar (request):
    mensaje="hola mundo"
    return HttpResponse(mensaje)

def fibonacci_hasta_100(request):
    serie=[]
    a,b=0,1

    while a<=100:
        serie.append(a)
        a,b=b,a+b

    return HttpResponse(serie)
    
def get_saldo(request):
    saldo=50000
    return HttpResponse(saldo)