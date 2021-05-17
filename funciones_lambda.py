def run():
    palindromo = lambda string: string == string[::-1]
    
    palabra = input("Ingresa una palabra->")
    
    if palindromo(palabra):
        print(f"{palabra} es un palíndromo")
    else:
        print(f"{palabra} no es un palíndromo")
        


if __name__ == '__main__':
    run()