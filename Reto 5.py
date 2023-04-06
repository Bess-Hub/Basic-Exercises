# Will attempt to perform a homework from Ely 

# Reto 5
## Escribe un programa que sea capaz de pedirle a un usuario por consola** que introduzca una contraseña y mientras que ésta no sea "admin", el programa seguirá pidiéndola
## Si la contraseña es errónea, deberá sacarle un mensaje de error y volver a pedirle la contraseña hasta que la introduzca bien. Si el usuario introduce "admin" correctamente, el programa le deberá mostrar un mensaje "Bienvenido al programa señor ADMIN" y luego terminar.
##NOTA: Para pedir por pantalla y guardarlo en una variable llamada password debes hacer uso de password:str = input('Introduce una contraseña')

password = ''

# Make a code so while the password is not equal to "Admin" to ask for the password. This means that if the input is equal to "Admin" it will proceed to the next step
while password != 'admin':
    password = input("Please type your password: ")
  # Indented to the while make a logical statement that if input is not "Admin" an error message would show. 
    if password != 'admin':
        print("Buuuh! Wrong password, please try again.")

# Once the while condition
print("Welcome back!")

# Success
