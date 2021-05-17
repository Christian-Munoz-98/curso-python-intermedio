def divisors(number):
    divisors = [i for i in range (1,number+1) if number % i == 0 ]
    return divisors

def run():
    number = int(input("Dame una cantidad---->>>>"))
    print(f"los divisores de {number} son {divisors(number)}")  

if __name__ == '__main__':
    run()