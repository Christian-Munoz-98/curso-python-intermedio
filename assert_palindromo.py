def palindromo(string):
    assert len(string) >0, "No se puede ingresar una cadena vacia"
    return string == string[::-1]

def run():
    
    string = input("Ingresa una palabra:")

    if palindromo(string):
        print("Es palindromo")
    else:
        print("No es palindromo")
        



if __name__ == '__main__':
    run()
    