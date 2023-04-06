# Will attempt to perform a homework from Ely that consists in creating a code capable of printing a sequence from 0 to 100 in reverse.

# Reto 4
## Escribe un programa que sea capaz de mostrar los elementos de una lista en orden inverso al original.
##Por ejemplo: teniendo [1,2,3,4,5] el programa debe mostrar por pantalla [5,4,3,2,1]

# Request the user to present the range of numbers of the list, the initial and the last number
num_ini = int((input("Indicate a starting number:")))
num_fin = int((input("Indicate an ending number:")))

# The user inputs will then form a list
numbers = [*range (num_ini, num_fin+1)]

# Then print it to confirm all numbers are there
print()
print('Original List: ', numbers)
print()

# Now reverse the list.
numbers.reverse()

# Now print the reversed list, add a string to indicate it is a reversed list just out of personal preference
print('Reversed List: ', numbers)
print()

# Success
