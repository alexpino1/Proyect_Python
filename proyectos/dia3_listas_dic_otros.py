"""1. pedir al usuario que escriba un texto (frase, poema lo que quiera)
dato de entrada
(almacenar en una lista, usar metodo upper o lower en el texto para la busqueda)
#2 pedir al usuario tres letras de su eleccion
2do dato de entrada(usar metodo upper o lower en el texto para la busqueda)
#analisis del programa para devolucion del usuario
1- cuantas veces aparece cada una de las letrass que el eligio
(realizar el metodo de substring para contar cuantas veces aparece un las
letras,este texto convertir cada string en una lista para la busqueda
y len para saber su largo)
2- informar cual es la primera, ultima leltra del texto al usuario
(usar metodo indexacion para esto)
3- invertir el orden de las palabras de esta lista y unirlos con espacion
 intermedios
4- validar si las palabras python se encuentran en este texto
(usar boolean)
"""
texto = input("Ingresa u ntexto a eleccion: ")
letras = []

texto = texto.lower()
letras.append(input("Ingresa la primera letras: ").lower())
letras.append(input("Ingresa la segunda letras: ").lower())
letras.append(input("Ingresa la tercera letras: ").lower())

print("\n")
print("Cantidad de letras")
cantidad_letras1 = texto.count(letras[0])
cantidad_letras2 = texto.count(letras[1])
cantidad_letras3 = texto.count(letras[2])

print(f"Hemos encontrado la letras{letras[0]} repetida {cantidad_letras1} veces")
print(f"Hemos encontrado la letras{letras[1]} repetida {cantidad_letras2} veces")
print(f"Hemos encontrado la letras{letras[2]} repetida {cantidad_letras3} veces")


print("\n")
print("Cantidad de palabras")
palabras = texto.split()
print(f"Hemos encontrado {len(palabras)} palabras en tu texto")

print("\n")
print("Letras de Inicio y de Fin")
letra_inicio = texto[0]
letra_final = texto[-1]
print(f"La letra inicial es '{letra_inicio}' y la letra final es '{letra_final}'")

print("\n")
print("Texto Invertido")
palabras.reverse()
texto_invertido = " ".join(palabras)
print(f"Si ordenamos tu texto alreves va decir: '{texto_invertido}'")

print("\n")
print("Buscando la palabra python")
buscar_python = "python" in texto
dic = {True: "si", False:"no"}
print(f"La palabra 'python'{dic[buscar_python]}se encuentra en el texto")
