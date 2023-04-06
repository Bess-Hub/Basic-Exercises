# Will attempt to perform a homework from Ely 

# Reto 11
## Escribe un programa que almacene en una lista (Array) todos los nombres de los alumnos del curso Programación para No Programadores y los muestre en por pantalla.

# First create a list of students
students = ["Michael", "George", "Diego", "Emma", "Fernando"]

# We can print the list of students like this:
print("The students name are:")
print(*students, sep="\n")
print()

# Or we can print it like this, I am exploring if there is any difference on using one or another
print("The students name are:")
for students in students:
    print(students)

# Success
