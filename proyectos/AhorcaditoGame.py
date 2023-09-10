from random import choice

palabras = ['panadero','dinosaurio','avioneta','chanclas']
letras_correctas =[]
letras_incorrectas = []
intentos = 6
aciertos = 0
juego_terminado = False

def palabra_aleatoria(lista_palabra):
    palabra_elegida = choice(lista_palabra)
    letras_unicas = len(set(palabra_elegida))
    return palabra_elegida,letras_unicas

def pedir_letra():
    letra_elegida = ''
    es_valia = False
    abecedario = 'abcdefghijklmnñopqrstuvwxyz'

    while not es_valia:
        letra_elegida =input('Elige una letras: ').lower()
        if letra_elegida in abecedario and len(letra_elegida) == 1:
            es_valia = True
        else:
            print('No has elegido una letra correcta')
    return letra_elegida

def Mostrar_tablero(palabra_elegida):

    lista_oculta = []

    for l in palabra_elegida:
        if l in letras_correctas:
            lista_oculta.append(l)
        else:
            lista_oculta.append('_')
    print(' '.join(lista_oculta))

def chequear_letra(letra_elegida, palabra_oculta, vidas, coincidencias):

    fin = False

    if letra_elegida in palabra_oculta:
        letras_correctas.append(letra_elegida)
        coincidencias  += 1
    else:
        letras_incorrectas.append(letra_elegida)
        vidas  -=1
    if vidas == 0:
        fin = perder()
    elif coincidencias == letras_unicas:
        fin = ganar(palabra_oculta)
    return vidas, fin, coincidencias

def perder():
    print('te has quedado sin vidas')
    print(f"La palabra oculta era + {palabras}")

    return True

def ganar(palabra_descubierta):
    Mostrar_tablero(palabra_descubierta)
    print('Felicidades has encontrado la palabra¡¡¡')
    return True


palabras, letras_unicas = palabra_aleatoria(palabras)

while not juego_terminado:
    print("\n"+ "*" * 20 + "\n")
    Mostrar_tablero(palabras)
    print("\n")
    print("letras incorrectas: "+ "-".join(letras_incorrectas))
    print(f"Vidas: {intentos}")
    print("\n" + "*" * 20 + "\n")
    letra = pedir_letra()

    intentos, terminado, aciertos = chequear_letra(letra, palabras, intentos, aciertos)

    juego_terminado = terminado