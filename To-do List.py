# Let's work with lists in this exercise, this example is a simple to-do list that already starts with basic tasks, more tasks can be added, and tasks can be removed.
# For this exercise, I did not use a template or a tutorial and tried to make it myself.
# Result in the end of the code.
to_do = ["Make bed", "Open curtains", "Make coffee"]

# Let's print the list so we know our starting point.
# If we just use the print function, we will get an ugly raw list.
print("Example of how a list looks like without the proper format:")
print(to_do)
print()

# But if our command contains a * before the list name and the , sep="\n" after it, it will print a nice line by line list.
print("Example of how we want a list to look like:")
print(*to_do, sep="\n")
print()

# Now let's say we want to make this dynamic, asking if something is to be added to or removed from our list.
to_add = ["add", "Add", "ADD"]
to_remove = ["remove", "Remove", "REMOVE"]

while True:
    initial_question = input("To add something to the list, please input ADD. To remove something from the list, please input REMOVE. To quit, please input QUIT: ")
    
    # If something is to be added.
    if initial_question in to_add:
        new_element = input("What do you want to add to the list? ")
        to_do.append(new_element)
        print()
        print(*to_do, sep="\n")
        print()
    
    # If something is to be removed.
    elif initial_question in to_remove:
        remove_element = input("What do you want to remove from the list? ")
        
        try:
            to_do.remove(remove_element)
            print()
            print(*to_do, sep="\n")
            print()
        except ValueError:
            print(f"{remove_element} not found in list. Please try again.")
            print()
        
    # If user wants to quit.
    elif initial_question == "QUIT":
        print("Quitting...")
        break
        
    else:
        print("Invalid input. Please try again.")
        print()

 # Success
