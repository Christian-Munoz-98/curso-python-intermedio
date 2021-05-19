def palindromo(string):
    return string == string[::-1]

def run():

    # string = input("Ingresa una palabra:")

    # if palindromo(string):
    #     print("Es palindromo")
    # else:
    #     print("No es palindromo")
    
    try:
        print(palindromo(1))
    except TypeError:
        print("Solo se pueden ingresar cadenas")



if __name__ == '__main__':
    run()
    