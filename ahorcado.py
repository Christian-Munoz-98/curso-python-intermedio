import random, os

def lista_palabras():
    with open("./archivos/data.txt", "r", encoding="utf-8") as f:
        palabras = [line.strip() for line in f]
    return palabras

def run():

    AHORCADO = ['''
      +---+
      |   |
          |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========''']

    palabra = random.choice(lista_palabras())
    palabra_secreta = "_" * len(palabra)
    palabra_secreta_control = list(palabra_secreta)
    errores = 0
    
    while errores < 10:
        # os.system("cls")
        print("AHORCADO")
        print(AHORCADO[errores])
        print(palabra_secreta)

        caracter = input(("\nEscribe una letra: "))
        if errores == 6 :
            print("Perdiste")
            break
        elif palabra == palabra_secreta:
            print(f"¡Felicidades, Gnaste!. La palabra es {palabra}")
            break
        elif len(caracter) != 1:
            print("Introduce una sola letra")
        elif caracter in palabra_secreta_control:
            print("Ya has elegido esa letra")
        elif caracter not in 'abcdefghijklmnopqrstuvwxyz':
            print ('Solo puedes ingresar letras')
        elif caracter not in palabra:
            errores += 1
        else:
            for i in range(len(palabra)):
                if caracter in palabra[i]:
                    palabra_secreta_control[i] = caracter
                    palabra_secreta = "".join(palabra_secreta_control)

if __name__ == '__main__':
    run()

