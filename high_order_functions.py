#Función "Filter"
'''
#Filtrando una lista con list comprehensions
my_list = [1, 4, 5, 6, 9, 13, 19, 21]
odd_comprehension = [i for i in my_list if i%2 != 0]
print(odd_comprehension)

#Uso con filter
my_list = [1,4,5,6,9,13,19,21]
odd = list(filter(lambda x: x%2 != 0, my_list))
print(odd)
'''
#Función "Map"

#Elevando una lista al cuadrado con list comprehension
my_list = [1,2,3,4,5]
squares = [i**2 for i in my_list ]
print(squares)

#Uso con Map
my_list = [1,2,3,4,5]
squares = list(map(lambda x: x**2, my_list))
print(squares)