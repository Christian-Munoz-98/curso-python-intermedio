import random 
import os

def lista_palabras():
    with open("./archivos/data.txt", "r", encoding="utf-8") as f:
        palabras = [line.strip() for line in f]
    return palabras

def run():
    print("Bienvenido al juego del ahorcado")
    palabra = random.choice(lista_palabras())
    palabra_secreta = "_" * len(palabra)
    palabra_secreta_control = list("_" * len(palabra))
    
    while palabra != palabra_secreta:

        os.system ("cls") 
        print("Bienvenido al juego del ahorcado")
        print(palabra_secreta)

        caracter = input(("\nEscribe una letra: "))

        for i in range(len(palabra)):
            if caracter == palabra[i]:
                palabra_secreta_control[i] = caracter
                palabra_secreta = "".join(palabra_secreta_control)
        print(f"¡Felicidades, Gnaste!. La palabra es {palabra}")

if __name__ == '__main__':
    run()