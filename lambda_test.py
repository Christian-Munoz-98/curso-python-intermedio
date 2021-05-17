#cuadrado de un número
sqr = lambda x: x**2
squares = []

for i in range (1,101):
    squares.append(sqr(i))

print(squares)

#facotrial con lambda
number = int(input("Dame un número ->"))
fact = lambda x: x**x