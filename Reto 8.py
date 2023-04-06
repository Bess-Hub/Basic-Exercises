# Will attempt to perform a homework from Ely 

# Reto 7
## Escribe un programa que pueda decirte si un número (número entero) es primo o no

# Now create a variable for the input text and ask for the user to input it
num_inp = int(input("Type a number: "))

# Ensure that the number is not lower than 0
if num_inp > 1:
    # Range all numbers between 2 and the input value
    for i in range(2, num_inp):
        if num_inp % i == 0:
            print(num_inp, "is not a prime number")
            break
    else:
        print(num_inp, "is a prime number")
else:
    print(num_inp, "is a prime number")
        
# Success
