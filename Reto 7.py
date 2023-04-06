# Will attempt to perform a homework from Ely 

# Reto 7
## Escribe un programa que contenga dos variables. Una de ellas representa la contraseña de un usuario y la otra un texto introducido. El programa debe poder mostrar por pantalla si las dos cadenas de texto son iguales sin tener en cuenta mayúsculas y minúsculas.

# First create a variable for the password
psw = "psw123"  

# Now create a variable for the input text and ask for the user to input it
input_psw = input("Type the password: ") 

# With if and else functions we create the conditions in which they match regardless if lowercase or uppercase
if input_psw.lower() == psw.lower():
    print("Password is correct")
else:
    print("Password is incorrect")

# Success
