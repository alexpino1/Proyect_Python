from random import *
numero = 0
nombre = input("Digite su nombre: ")
intentos = 8
print("Bueno, Juan, he pensado un número entre 1 y 100, y tienes solo ocho intentos"+
       "para adivinar cuál crees que es el número")
aleatorio_numero = randint(1,7)
while intentos > 0:
    numero = int(input("Adivina un numero: "))
    if numero < 1 or numero > 100:
         print("has elegido un número que no está permitido")
    elif numero < aleatorio_numero:
        print("su respuesta es incorrecta y que ha elegido un número menor al número secreto")
    elif numero > aleatorio_numero:
        print("su respuesta es incorrecta y que ha elegido un número mayor al número secreto")
    else:
        print(f"Acertaste  el numero {nombre} has ganado en : {intentos} intentos")
        break
    intentos -= 1

if intentos == 0 :
    print(f"Perdiste, Agotaste la cantidad de intentos el numero era {aleatorio_numero}")