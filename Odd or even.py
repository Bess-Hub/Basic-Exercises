# Simple exercise to determine if a number that the user input is odd or even.
# Made from scratch, learned the remainder sign "%".
# Used the While funtion that I learned when building the Hang Man Game - This is why it is good to follow tutorials and understand the logic behind the code.

# Lets make a self-explanatory header
print("Let's find out if a number is odd or even")
print()

# Add the input function with the question
user_number = int(input("What is the number? "))

# Lets work the variables

# Fot a number to be even it must be divisible by 2, meaning that the remainder must be 0
if user_number%2 == 0:
  print(f"The number - ",user_number," - is even")
  print()
else :
  print(f"The number - ",user_number," - is odd")
  print()

# Now lets make a code for it to ask if we want to go again
while input("Another one? Y/N ").upper() == "Y" or ("y"):
  print() 
  print("Let's find out if a number is odd or even")
  print()
  user_number = int(input("What is the number? "))
  if user_number%2 == 0:
    print(f"The number - ",user_number," - is even")
    print()
  else :
    print(f"The number - ",user_number," - is odd")
    print()
    
# It worked, but how do I put an end or create a condition for when Another one is "N"? I hope to laught at this question one day...
