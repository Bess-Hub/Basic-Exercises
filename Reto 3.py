# Will attempt to perform a homework from Ely that consists in creating a code capable of printing a sequence from 0 to 100 in reverse.

# Reto 3
# Escribe un programa que sea capaz de mostrar los números del 1 al 100 en orden inverso.

# First create a list that consists of a range, since the last element is not inclusive of we add as it +1
numbers = [*range (0, 100+1)]

# Then print it to confirm all numbers are there
print(numbers)
print()

# Now reverse the list.
numbers.reverse()

# Now print the reversed list, add a string to indicate it is a reversed list just out of personal preference
print('Reversed List: ', numbers)
print()

# Success
