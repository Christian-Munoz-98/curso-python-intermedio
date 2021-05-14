def run():
    '''
    squares = []
    for i in range(1,101):
        if i % 3 != 0:
            squares.append(i**2)
    
    squares = [i**2 for i in range(1,101) if i%3 != 0]
    print(squares)
    '''
    #Reto
    #Crear, con un list comprehension, una lista de todos los múltiplos de 4 que la vez también son múltiplos de 6 y de 9, hasta 5 digitos.

    multiples = [i for i in range (1,100000) if i % 36 == 0 ]
    print(multiples)

if __name__ == '__main__':
    run()