def divisors(number):
    divisors = [i for i in range (1,number+1) if number % i == 0 ]
    return divisors

def run():
    try:
        number = int(input("Dame una cantidad---->>>>"))
        if number < 0:
            raise Exception ('No se permiten numeros negativos')
        print(f"los divisores de {number} son {divisors(number)}")  
        print("Termino mi programa")
    except ValueError:
        print("Debes ingresar un numero")
    except Exception:
        print("No se permiten numeros negativos")


if __name__ == '__main__':
    run()