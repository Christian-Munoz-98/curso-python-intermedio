def palindromo(string):
    return string == string[::-1]

def run():
    try:
        string = input("Ingresa una palabra:")

        if palindromo(string):
            print("Es palindromo")
        else:
            print("No es palindromo")
        if type(int(string)) == int:
            raise ValueError("No se permiten numeros")

    except ValueError:
        print("Solo se pueden ingresar cadenas")



if __name__ == '__main__':
    run()
    