diccionario = {
    "hola": "hello",
    "adiós": "goodbye",
    "gracias": "thank you",
    "por favor": "please",
    "perro": "dog",
    "gato": "cat",
    "casa": "house",
    "escuela": "school",
    "libro": "book",
    "mesa": "table",
    "silla": "chair",
    "coche": "car",
    "ciudad": "city",
    "comida": "food",
    "agua": "water",
    "amigo": "friend",
    "familia": "family",
    "trabajo": "work",
    "dinero": "money",
    "tiempo": "time",
    "día": "day",
    "noche": "night",
    "sol": "sun",
    "luna": "moon",
    "mar": "sea",
    "montaña": "mountain",
    "feliz": "happy",
    "triste": "sad",
    "rápido": "fast",
    "lento": "slow"
}

print("Traductor virtual de palabras...")
while palabra!="0":
 palabra=input("Ingrese la palabra en español(cero para terminar): ")
 if palabra == "0" :
    print("Traductor cerrado,Muchas gracias!!")
 elif palabra in diccionario:
    print("traduccion:" , diccionario[palabra])
 else:
    opcion=input("Su palabra no se encuentra aqui,desea agregar al diccionario (Si/No): ")
    if opcion == "Si":
        traduccion=input("Ingrese la palabra en ingles: ")
        diccionario[palabra]=traduccion
    elif opcion == "No":
        print("Ok,no lo vamos a agregar.")    