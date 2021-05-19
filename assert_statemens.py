def divisors(number):
    divisors = [i for i in range (1,number+1) if number % i == 0 ]
    return divisors

# def run():
    
#     number = (input("Dame una cantidad---->>>>"))
#     assert number.isnumeric(), "Debes ingresar un numero"
#     print(f"los divisores de {int(number)} son {divisors(int(number))}")  
#     print("Termino mi programa")

def run():
    
    number = int(input("Dame una cantidad---->>>>"))
    assert number > 0, "Debes ingresar un numero positivo"
    print(f"los divisores de {number} son {divisors(number)}")  
    print("Termino mi programa")



if __name__ == '__main__':
    run()