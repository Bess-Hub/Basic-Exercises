# Will attempt to perform a homework from Ely 

# Reto 9
## Escribe un programa que pueda decirte si un año (número entero) es bisiesto o no

# We can assume that a year, to be a leap year, must be divisible by 4
# Now create a variable for the input year:
input_year = int(input("Type the year: "))

# With if and else functions we create the conditions in which they match regardless if lowercase or uppercase
if input_year % 4 == 0:
    print(input_year, "is a leap year")
else:
    print(input_year, "is not a leap year")

# Success
