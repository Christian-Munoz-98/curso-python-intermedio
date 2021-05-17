#Filtrando una lista con list comprehensions
my_list = [1, 4, 5, 6, 9, 13, 19, 21]
odd_comprehension = [i for i in my_list if i%2 != 0]
print(odd_comprehension)

#Uso con filter
my_list = [1,4,5,6,9,13,19,21]
odd = list(filter(lambda x: x%2 != my_list))
print(odd)
