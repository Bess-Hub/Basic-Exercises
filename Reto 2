# Will attempt to perform a homework from Ely that consists in creating a code capable of printing all even numbers from a starting value to an end value

## Reto 2
### Escribe un programa capaz de mostrar todos los números impares desde un número de inicio y otro final.
### Por ejemplo: teniendo numero_inicial = 2 y numero_final = 8, el programa debe imprimir por consola: [3, 5, 7]

# This is somehow similar to my Odd or Even exercise so I would start by requesting the user to present the range, the initial and the last number
num_ini = int((input("Indicate a starting number:")))
num_fin = int((input("Indicate an ending number:")))

# The user inputs will then form a list
numbers = [*range (num_ini, num_fin+1)]

# We can test if it does by printing it
print("All numbers: ", numbers)
print()

# From all methods tried Comprehension was the simplest one
even_list = [ i for i in numbers if i%2 == 0]
print('Even numbers: ', even_list)

#Success
