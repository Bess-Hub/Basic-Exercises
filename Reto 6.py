# Will attempt to perform a homework from Ely 

# Reto 6
##Escribe un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.

# Create a variable age that will be the input from the user to the question "What is your age?"
age = int(input("What is your age? "))

# Create the variables for if the age value is less than 18 to print the message that the person is a minor.
if age < 18:
    print("You are a minor.")

# Create a variable that if the age is not less than 18 to print the message that the person is not a minor.
else:
  print("You are not a minor.")
  
# Success
